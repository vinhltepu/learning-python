from extensions import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(30), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    total_spent = db.Column(db.Float, nullable=False, default=0)

    # inheritance
    customer_type = db.Column(db.String(50), nullable=False, default="regular")

    __mapper_args__ = {
        "polymorphic_on": customer_type,
        "polymorphic_identity": "regular",
    }

    def validate(self):
        if not self.name or not self.phone or not self.address:
            raise ValueError("Vui lòng nhập đủ: Tên, SĐT, Địa chỉ.")
        if self.total_spent < 0:
            raise ValueError("Tổng tiền đã mua không được âm.")

    def discount_rate(self) -> float:
        return 0.0

class RegularCustomer(Customer):
    __mapper_args__ = {"polymorphic_identity": "regular"}

class VIPCustomer(Customer):
    __mapper_args__ = {"polymorphic_identity": "vip"}

    def discount_rate(self) -> float:
        if self.total_spent >= 200_000_000:
            return 0.10
        if self.total_spent >= 100_000_000:
            return 0.05
        return 0.0