
class Customer:

    def __init__(self, id=None, name="", phone="", address="", total_spent=0.0, customer_type="regular"):
        self.id = id
        self.name = (name or "").strip()
        self.phone = (phone or "").strip()
        self.address = (address or "").strip()
        self.total_spent = float(total_spent or 0)
        self.customer_type = customer_type or "regular"

        # validate cơ bản
        if not self.name or not self.phone or not self.address:
            raise ValueError("tên/SĐT/Địa chỉ không được để trống")
        if self.total_spent < 0:
            raise ValueError("tổng tiền đã mua không được âm")

    # polymorphism: lớp con override
    def discount_rate(self) -> float:
        return 0.0

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "address": self.address,
            "total_spent": self.total_spent,
            "customer_type": self.customer_type,
            "discount_rate": self.discount_rate(),
        }


class RegularCustomer(Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, customer_type="regular", **kwargs)


class VIPCustomer(Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, customer_type="vip", **kwargs)
    def discount_rate(self) -> float:
        if self.total_spent >= 200_000_000:
            return 0.10
        if self.total_spent >= 100_000_000:
            return 0.05
        return 0.0


def customer_from_row(row):
    ctype = (row["customer_type"] if "customer_type" in row.keys() else row.get("customer_type")) or "regular"

    base_kwargs = dict(
        id=row["id"] if "id" in row.keys() else row.get("id"),
        name=row["name"] if "name" in row.keys() else row.get("name"),
        phone=row["phone"] if "phone" in row.keys() else row.get("phone"),
        address=row["address"] if "address" in row.keys() else row.get("address"),
        total_spent=row["total_spent"] if "total_spent" in row.keys() else row.get("total_spent", 0),
    )

    if ctype == "vip":
        return VIPCustomer(**base_kwargs)
    return RegularCustomer(**base_kwargs)

#Thêm, sửa, xóa, tìm kiếm. 
class CustomerService:
    def get_all(self, q: str | None = None):
        conn = connect()
        cur = conn.cursor()

        if q:
            like = f"%{q.strip()}%"
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
        return [customer_from_row(r) for r in rows]

    def get(self, cid: int):
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
        return customer_from_row(row) if row else None

    def create_from_form(self, form):
       
        name = (form.get("name") or "").strip()
        phone = (form.get("phone") or "").strip()
        address = (form.get("address") or "").strip()

        total_spent_raw = form.get("total_spent") or "0"
        total_spent = float(total_spent_raw or 0)

        ctype = (form.get("customer_type") or "").strip().lower()
        if not ctype:
            ctype = "vip" if total_spent >= 100_000_000 else "regular"

        if ctype == "vip":
            return VIPCustomer(name=name, phone=phone, address=address, total_spent=total_spent)
        return RegularCustomer(name=name, phone=phone, address=address, total_spent=total_spent)

    def add(self, customer: Customer):
        conn = connect()
        cur = conn.cursor()

        try:
            cur.execute(
                """
                INSERT INTO customers(name, phone, address, total_spent, customer_type)
                VALUES (?, ?, ?, ?, ?)
                """,
                (customer.name, customer.phone, customer.address, customer.total_spent, customer.customer_type),
            )
            conn.commit()
            customer.id = cur.lastrowid
            conn.close()
            return customer
        except sqlite3.IntegrityError:
            conn.rollback()
            conn.close()
            return None

    def update(self, customer: Customer):
        """
        Update theo object 
        """
        conn = connect()
        cur = conn.cursor()

        try:
            cur.execute(
                """
                UPDATE customers
                SET name = ?, phone = ?, address = ?, total_spent = ?, customer_type = ?
                WHERE id = ?
                """,
                (customer.name, customer.phone, customer.address, customer.total_spent, customer.customer_type, customer.id),
            )
            conn.commit()
            ok = (cur.rowcount > 0)
            conn.close()
            return ok
        except sqlite3.IntegrityError:
            conn.rollback()
            conn.close()
            return False

    def update_from_form(self, customer: Customer, form):
        
        name = (form.get("name") or "").strip()
        phone = (form.get("phone") or "").strip()
        address = (form.get("address") or "").strip()

        total_spent_raw = form.get("total_spent") or "0"
        total_spent = float(total_spent_raw or 0)

        ctype = (form.get("customer_type") or customer.customer_type or "regular").strip().lower()

        base_kwargs = dict(
            id=customer.id,
            name=name,
            phone=phone,
            address=address,
            total_spent=total_spent,
        )

        new_customer = VIPCustomer(**base_kwargs) if ctype == "vip" else RegularCustomer(**base_kwargs)
        self.update(new_customer)
        return new_customer

    def delete(self, cid_or_customer):
        cid = cid_or_customer.id if hasattr(cid_or_customer, "id") else int(cid_or_customer)

        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM customers WHERE id = ?", (cid,))
        conn.commit()
        ok = (cur.rowcount > 0)
        conn.close()
        return ok