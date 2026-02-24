from datetime import datetime
from extensions import db
from models.invoice import Invoice, InvoiceItem
from models.customer import Customer
from models.product import Product

class InvoiceService:
    def get_all(self, customer_id: int | None = None, date_from: str | None = None, date_to: str | None = None):
        query = Invoice.query

        if customer_id:
            query = query.filter(Invoice.customer_id == customer_id)

        def parse_dt(s):
            try:
                return datetime.strptime(s, "%Y-%m-%d")
            except:
                return None

        df = parse_dt(date_from) if date_from else None
        dt = parse_dt(date_to) if date_to else None

        if df:
            query = query.filter(Invoice.created_at >= df)
        if dt:
            dt_end = dt.replace(hour=23, minute=59, second=59)
            query = query.filter(Invoice.created_at <= dt_end)

        return query.order_by(Invoice.id.desc()).all()

    def create_invoice(self, customer_id: int, cart: dict[int, int]) -> int:
        if not cart:
            raise ValueError("Giỏ hàng trống")

        customer = Customer.query.get(customer_id)
        if not customer:
            raise ValueError("Không tìm thấy khách hàng")

        items = []
        subtotal = 0.0

        # 1) check tồn kho + tính tiền
        for pid, qty in cart.items():
            if qty <= 0:
                continue

            p = Product.query.get(pid)
            if not p:
                raise ValueError(f"Sản phẩm id={pid} không tồn tại")
            if p.stock < qty:
                raise ValueError(f"Không đủ hàng cho {p.name} (còn {p.stock}, cần {qty})")

            unit_price = float(p.sell_price or 0)
            line_total = unit_price * qty
            subtotal += line_total
            items.append((p, qty, unit_price, line_total))

        if not items:
            raise ValueError("Bạn chưa chọn sản phẩm nào (qty > 0)")

        # 2) giảm giá theo VIPCustomer.discount_rate()
        discount_rate = customer.discount_rate()
        discount_amount = subtotal * discount_rate
        total = subtotal - discount_amount

        # 3) tạo invoice + items + trừ kho + cộng điểm
        try:
            inv = Invoice(
                customer_id=customer.id,
                subtotal=subtotal,
                discount_rate=discount_rate,
                discount_amount=discount_amount,
                total=total,
            )
            db.session.add(inv)
            db.session.flush()  # lấy inv.id

            for p, qty, unit_price, line_total in items:
                db.session.add(InvoiceItem(
                    invoice_id=inv.id,
                    product_id=p.id,
                    qty=qty,
                    unit_price=unit_price,
                    line_total=line_total
                ))
                p.stock -= qty

            customer.total_spent += total

            # auto chuyển VIP nếu >=100tr
            if customer.total_spent >= 100_000_000:
                customer.customer_type = "vip"

            db.session.commit()
            return inv.id
        except Exception:
            db.session.rollback()
            raise

    def get_detail(self, invoice_id: int):
        inv = Invoice.query.get(invoice_id)
        if not inv:
            return None, []
        return inv, inv.items