from datetime import datetime
from app import db

class Invoice(db.Model):
    __tablename__ = 'invoices'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    subtotal = db.Column(db.Float, default=0)
    discount_rate = db.Column(db.Float, default=0)
    total_amount = db.Column(db.Float, default=0)

    # tạo mối liên hệ 
    customer = db.relationship("Customer")
    details = db.relationship("InvoiceDetail", backref="invoice", cascade="all, delete-orphan")

    def calculate_total(self):
        """Tính tổng tiền hóa đơn dựa trên các chi tiết và áp dụng giảm giá."""
        self.subtotal = sum(detail.line_total for detail in self.details)
        if self.customer:
            self.discount_rate = self.customer.get_discount_rate()
        else:
            self.discount_rate = 0
        self.total_amount = self.subtotal * (1 - self.discount_rate)
        return self.total_amount

    @classmethod
    def revenue_by_day(cls):
        """Thống kê doanh thu theo ngày."""
        result = db.session.query(
            db.func.date(cls.created_at),
            db.func.sum(cls.total_amount)
        ).group_by(
            db.func.date(cls.created_at)
        ).all()
        return result

    def show_invoice_info(self):
        """Trả về chuỗi thông tin cơ bản của hóa đơn."""
        return f"Invoice ID: {self.id}, Customer ID: {self.customer_id}, Total: {self.total_amount:.2f}"

class InvoiceDetail(db.Model):
    """Lớp chi tiết hóa đơn, lưu thông tin từng sản phẩm trong hóa đơn."""
    __tablename__ = "invoice_details"

    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey("invoices.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    line_total = db.Column(db.Float, nullable=False)

    # Mối quan hệ với Product
    product = db.relationship("Product")

    def __init__(self, product_id, quantity, unit_price):
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.line_total = self.quantity * self.unit_price

    def show_detail_info(self):
        """Trả về chuỗi thông tin chi tiết của dòng hóa đơn."""
        return f"Product ID: {self.product_id}, Quantity: {self.quantity}, Unit Price: {self.unit_price:.2f}"
