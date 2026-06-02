
from app import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    total_spent = db.Column(db.Float, default=0.0)

    __mapper_args__ = {
        "polymorphic_identity": "customer",
        "polymorphic_on": type
    }

    invoices = db.relationship("Invoice", backref="customer", lazy=True)

    def __init__(self, name, phone, address, total_spent=0):
        self.name = name
        self.phone = phone
        self.address = address
        self.total_spent = total_spent

    @staticmethod
    def is_valid_phone(phone):
        if not phone:
            return False
        cleaned = phone.strip()
        return cleaned.isdigit() and len(cleaned) >= 9

    @property
    def customer_name(self):
        return self.name

    @customer_name.setter
    def customer_name(self, value):
        if value and len(value.strip()) >= 2:
            self.name = value.strip()
        else:
            raise ValueError("Invalid customer name. Name must be at least 2 characters long.")

    @property
    def points(self):
        return self.total_spent

    @points.setter
    def points(self, new_points):
        if float(new_points) >= 0:
            self.total_spent = float(new_points)
        else:
            raise ValueError("Điểm tích lũy không được âm")

    @points.deleter
    def points(self):
        self.total_spent = 0

    def add_spending(self, money):
        if money > 0:
            self.total_spent += money
        else:
            raise ValueError("Số tiền phải lớn hơn 0")

    def get_discount_rate(self):
        return 0

    def show_customer_info(self):
        return f"Khách hàng: {self.name} - Số điện thoại: {self.phone}"


class RegularCustomer(Customer):
    __tablename__ = "regular_customers"

    id = db.Column(db.Integer, db.ForeignKey("customers.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "regular"
    }

    def get_discount_rate(self):
        return 0


class VIPCustomer(Customer):
    __tablename__ = "vip_customers"

    id = db.Column(db.Integer, db.ForeignKey("customers.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "vip"
    }

    def get_discount_rate(self):
        if self.total_spent >= 200000000:
            return 0.10
        if self.total_spent >= 100000000:
            return 0.05
        return 0
