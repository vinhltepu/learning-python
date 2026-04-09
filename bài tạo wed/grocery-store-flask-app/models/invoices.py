from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from . import Base

# Định nghĩa model Invoice cho bảng invoices trong cơ sở dữ liệu
class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    goods_list = Column(Float, nullable=False)  # This could be a JSON or a separate model in a real application
    total_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="invoices")
