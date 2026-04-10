from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from . import Base
# Định nghĩa model Invoice cho bảng invoices trong cơ sở dữ liệu
class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    total_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # thiết lập mối quan hệ với bảng customers
    customer = relationship('Customer', back_populates='invoices')