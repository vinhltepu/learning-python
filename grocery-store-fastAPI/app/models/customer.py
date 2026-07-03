from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.base import Base

# Đây là model Customer, đại diện cho bảng customers trong database, có các trường id, name, phone,
# address, total_spent và mối quan hệ với bảng invoices thông qua relationship.
# Dùng Single Table Inheritance: lớp con RegularCustomer và VIPCustomer lưu chung 1 bảng,
# phân biệt nhau qua cột customer_type.
class Customer(Base):
    __tablename__ = "customers"
    id            = Column(Integer, primary_key=True, index=True)
    name          = Column(String(255), nullable=False)
    phone         = Column(String(20),  nullable=False, unique=True, index=True)
    address       = Column(String(500), nullable=True)
    total_spent   = Column(Float,       nullable=False, default=0.0)
    # cột phân biệt loại khách hàng để SQLAlchemy biết map sang lớp con nào
    customer_type = Column(String(20),  nullable=False)
    # relationship with Invoice model
    invoices = relationship("Invoice", back_populates="customer")
# thêm __mapper_args__ vì liên quan đến kế thừa 
    __mapper_args__ = {
        "polymorphic_on":       customer_type,
        "polymorphic_identity": "regular",
    }

    def get_discount_rate(self) -> float:
        """Mặc định không có giảm giá."""
        return 0.0
#lớp con khách thường, không giảm giá 
class RegularCustomer(Customer):
    __mapper_args__ = {
        "polymorphic_identity": "regular_customer",
    }
# lớp con giảm giá theo tổng tiền dã chi tiêu
class VIPCustomer(Customer):
    __mapper_args__ = {
        "polymorphic_identity": "vip",
    }

    def get_discount_rate(self) -> float:
        if self.total_spent >= 200_000_000:
            return 0.10
        elif self.total_spent >= 100_000_000:
            return 0.05
        return 0.0