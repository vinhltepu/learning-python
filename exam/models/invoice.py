from datetime import datetime
from extensions import db

class Invoice(db.Model):
    __tablename__ = "invoices"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    customer = db.relationship("Customer", backref="invoices")

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    subtotal = db.Column(db.Float, nullable=False, default=0)
    discount_rate = db.Column(db.Float, nullable=False, default=0)
    discount_amount = db.Column(db.Float, nullable=False, default=0)
    total = db.Column(db.Float, nullable=False, default=0)

class InvoiceItem(db.Model):
    __tablename__ = "invoice_items"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    invoice_id = db.Column(db.Integer, db.ForeignKey("invoices.id", ondelete="CASCADE"), nullable=False)
    invoice = db.relationship(
        "Invoice",
        backref=db.backref("items", cascade="all, delete-orphan")
    )

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    product = db.relationship("Product")

    qty = db.Column(db.Integer, nullable=False, default=1)
    unit_price = db.Column(db.Float, nullable=False, default=0)
    line_total = db.Column(db.Float, nullable=False, default=0)