
import sqlite3
from db import connect
from models.customer import Customer, customer_from_row


class CustomerService:
    def get_all(self, q: str = ""):
        conn = connect()
        cur = conn.cursor()

        q = (q or "").strip()
        if q:
            like = f"%{q}%"
            cur.execute(
                """
                SELECT id, name, phone, address, total_spent, customer_type
                FROM customers
                WHERE name LIKE ? OR phone LIKE ?
                ORDER BY id DESC
                """,
                (like, like),
            )
        else:
            cur.execute(
                """
                SELECT id, name, phone, address, total_spent, customer_type
                FROM customers
                ORDER BY id DESC
                """
            )

        rows = cur.fetchall()
        conn.close()

        # sqlite3.Row không có .get() => đổi sang dict trước
        return [customer_from_row(dict(r)) for r in rows]

    def get_by_id(self, cid: int):
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT id, name, phone, address, total_spent, customer_type
            FROM customers
            WHERE id = ?
            """,
            (cid,),
        )
        row = cur.fetchone()
        conn.close()
        return customer_from_row(dict(row)) if row else None

    def add(self, customer: Customer) -> bool:
        conn = connect()
        cur = conn.cursor()
        try:
            cur.execute(
                """
                INSERT INTO customers(name, phone, address, total_spent, customer_type)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    customer.name,
                    customer.phone,
                    customer.address,
                    customer.total_spent,
                    customer.customer_type,
                ),
            )
            conn.commit()
            # cập nhật id cho object
            customer._Customer__dict__ if False else None  
            customer._id = cur.lastrowid
            conn.close()
            return True
        except sqlite3.IntegrityError:
            conn.rollback()
            conn.close()
            return False

    def update(self, customer: Customer) -> bool:
        conn = connect()
        cur = conn.cursor()
        try:
            cur.execute(
                """
                UPDATE customers
                SET name=?, phone=?, address=?, total_spent=?, customer_type=?
                WHERE id=?
                """,
                (
                    customer.name,
                    customer.phone,
                    customer.address,
                    customer.total_spent,
                    customer.customer_type,
                    customer.id,
                ),
            )
            conn.commit()
            ok = cur.rowcount > 0
            conn.close()
            return ok
        except sqlite3.IntegrityError:
            conn.rollback()
            conn.close()
            return False

    def delete(self, cid: int) -> bool:
        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM customers WHERE id = ?", (cid,))
        conn.commit()
        ok = cur.rowcount > 0
        conn.close()
        return ok
