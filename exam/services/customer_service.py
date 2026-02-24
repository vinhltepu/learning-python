from sqlalchemy.exc import IntegrityError
from extensions import db
from models.customer import Customer, RegularCustomer, VIPCustomer

class CustomerService:
    def get_all(self, q: str | None = None):
        query = Customer.query
        if q:
            like = f"%{q.strip()}%"
            query = query.filter((Customer.name.ilike(like)) | (Customer.phone.ilike(like)))
        return query.order_by(Customer.id.desc()).all()

    def get(self, cid: int):
        return Customer.query.get(cid)

    def _auto_type(self, total_spent: float) -> str:
        return "vip" if total_spent >= 100_000_000 else "regular"

    def create_from_form(self, form):
        total_spent = float(form.get("total_spent") or 0)

        ctype = (form.get("customer_type") or "").strip().lower()
        if not ctype:
            ctype = self._auto_type(total_spent)

        cls = VIPCustomer if ctype == "vip" else RegularCustomer

        c = cls(
            name=(form.get("name") or "").strip(),
            phone=(form.get("phone") or "").strip(),
            address=(form.get("address") or "").strip(),
            total_spent=total_spent,
        )

        c.validate()
        return c

    def add(self, customer: Customer):
        try:
            db.session.add(customer)
            db.session.commit()
            return customer
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Số điện thoại đã tồn tại (bị trùng).")

    def update_from_form(self, customer: Customer, form):
        customer.name = (form.get("name") or "").strip()
        customer.phone = (form.get("phone") or "").strip()
        customer.address = (form.get("address") or "").strip()
        customer.total_spent = float(form.get("total_spent") or 0)

        ctype = (form.get("customer_type") or "").strip().lower()
        if not ctype:
            ctype = self._auto_type(customer.total_spent)
        customer.customer_type = ctype

        customer.validate()

        try:
            db.session.commit()
            return customer
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Số điện thoại bị trùng.")

    def delete(self, customer: Customer):
        db.session.delete(customer)
        db.session.commit()