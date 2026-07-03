from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base

class Invoice(Base):
    __tablename__ = "invoices"
    id            = Column(Integer, primary_key=True, index=True)
    # tạo khóa ngoại liên kết với bảng customers, ondelete="RESTRICT" ngăn xóa khách hàng nếu còn hóa đơn
    customer_id   = Column(Integer, ForeignKey("customers.id", ondelete="RESTRICT"), nullable=False)
    # tự động ghi thời gian tạo bản ghi, sử dụng func.now() để lấy thời gian hiện tại từ database
    created_at    = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    total_amount  = Column(Float, nullable=False, default=0.0)   # tổng tiền trước giảm giá
    discount_rate = Column(Float, nullable=False, default=0.0)   # % giảm giá áp dụng
    final_amount  = Column(Float, nullable=False, default=0.0)   # tổng tiền sau giảm giá
    # relationship with Customer model
    customer = relationship("Customer", back_populates="invoices")
    # relationship with InvoiceDetail model
    details  = relationship("InvoiceDetail", back_populates="invoice")

# từng dòng sản phẩm trong hóa đơn, liên kết với bảng invoices và products thông qua relationship.
class InvoiceDetail(Base):
    __tablename__ = "invoice_details"
    id         = Column(Integer, primary_key=True, index=True)
    # tạo các khóa ngoại liên kết với bảng invoices và products
    invoice_id = Column(Integer, ForeignKey("invoices.id",  ondelete="CASCADE"),  nullable=False)
    product_id = Column(Integer, ForeignKey("products.id",  ondelete="RESTRICT"), nullable=False)
    quantity   = Column(Integer, nullable=False)
    unit_price = Column(Float,   nullable=False)   # giá tại thời điểm bán
    subtotal   = Column(Float,   nullable=False)   # quantity * unit_price
    # tạo relationship with Invoice và Product
    invoice = relationship("Invoice", back_populates="details")
    product = relationship("Product", back_populates="invoice_details")