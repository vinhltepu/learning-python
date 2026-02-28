import sqlite3
from db import connect


class InvoiceService:
    def _vip_discount_rate(self, total_spent: float) -> float:
        # đúng yêu cầu: >100tr 5%, >200tr 10%
        if total_spent >= 200_000_000:
            return 0.10
        if total_spent >= 100_000_000:
            return 0.05
        return 0.0

    def create_invoice(self, customer_id: int, cart: dict):
        """
        cart: dict {product_id: qty}, qty > 0
        - kiểm tra tồn kho
        - tính subtotal
        - áp giảm giá (nếu VIP)
        - trừ tồn kho
        - lưu invoices + invoice_items
        - cập nhật total_spent của customer
        """
        if not cart:
            raise ValueError("Giỏ hàng trống")

        conn = connect()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        try:
            # 1) lấy thông tin customer
            cur.execute("SELECT id, total_spent, customer_type FROM customers WHERE id=?", (customer_id,))
            customer = cur.fetchone()
            if not customer:
                raise ValueError("Không tìm thấy khách hàng")

            total_spent = float(customer["total_spent"] or 0)
            customer_type = customer["customer_type"] or "regular"

            discount_rate = 0.0
            if customer_type == "vip":
                discount_rate = self._vip_discount_rate(total_spent)

            # 2) duyệt cart để tính tiền + kiểm tra stock
            subtotal = 0.0
            items = []  # list of (product_id, qty, unit_price, line_total)

            for pid, qty in cart.items():
                qty = int(qty)
                if qty <= 0:
                    continue

                cur.execute("SELECT id, sell_price, stock FROM products WHERE id=?", (pid,))
                p = cur.fetchone()
                if not p:
                    raise ValueError(f"Sản phẩm id={pid} không tồn tại")

                stock = int(p["stock"] or 0)
                if stock < qty:
                    raise ValueError(f"Không đủ hàng cho sản phẩm id={pid} (còn {stock}, cần {qty})")

                unit_price = float(p["sell_price"] or 0)
                line_total = unit_price * qty
                subtotal += line_total
                items.append((pid, qty, unit_price, line_total))

            if not items:
                raise ValueError("Bạn chưa chọn sản phẩm nào (qty > 0)")

            discount_amount = subtotal * discount_rate
            total = subtotal - discount_amount

            # 3) tạo invoice
            cur.execute("""
                INSERT INTO invoices(customer_id, subtotal, discount_rate, discount_amount, total)
                VALUES (?, ?, ?, ?, ?)
            """, (customer_id, subtotal, discount_rate, discount_amount, total))
            invoice_id = cur.lastrowid

            # 4) tạo invoice_items + trừ tồn kho
            for pid, qty, unit_price, line_total in items:
                cur.execute("""
                    INSERT INTO invoice_items(invoice_id, product_id, qty, unit_price, line_total)
                    VALUES (?, ?, ?, ?, ?)
                """, (invoice_id, pid, qty, unit_price, line_total))

                # trừ tồn kho
                cur.execute("""
                    UPDATE products
                    SET stock = stock - ?
                    WHERE id = ?
                """, (qty, pid))

            # 5) cộng điểm tích lũy (tổng tiền đã mua)
            cur.execute("""
                UPDATE customers
                SET total_spent = total_spent + ?
                WHERE id = ?
            """, (total, customer_id))

            conn.commit()
            conn.close()
            return invoice_id

        except Exception:
            conn.rollback()
            conn.close()
            raise

    def get_all(self):
        conn = connect()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("""
            SELECT i.id, i.created_at, i.customer_id, c.name AS customer_name,
                   i.subtotal, i.discount_amount, i.total
            FROM invoices i
            JOIN customers c ON c.id = i.customer_id
            ORDER BY i.id DESC
        """)
        rows = cur.fetchall()
        conn.close()
        return rows

    def get_detail(self, invoice_id: int):
        conn = connect()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("""
            SELECT i.*, c.name AS customer_name, c.phone AS customer_phone
            FROM invoices i
            JOIN customers c ON c.id = i.customer_id
            WHERE i.id = ?
        """, (invoice_id,))
        invoice = cur.fetchone()

        cur.execute("""
            SELECT it.*, p.name AS product_name, p.code AS product_code
            FROM invoice_items it
            JOIN products p ON p.id = it.product_id
            WHERE it.invoice_id = ?
        """, (invoice_id,))
        items = cur.fetchall()

        conn.close()
        return invoice, items