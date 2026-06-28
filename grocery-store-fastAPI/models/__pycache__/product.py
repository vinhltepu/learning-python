from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base

class Product(Base):
    __tablename__ = "products"
    id            = Column(Integer, primary_key=True, index=True)
    name          = Column(String(255), nullable=False)
    code          = Column(String(100), nullable=False, unique=True, index=True)
    unit          = Column(String(50),  nullable=False)
    import_price  = Column(Float,       nullable=False)
    selling_price = Column(Float,       nullable=False)
    stock         = Column(Integer,     nullable=False, default=0)
    import_date   = Column(DateTime(timezone=True), server_default=func.now())
    # cột phân biệt loại sản phẩm để SQLAlchemy biết map sang lớp con nào
    product_type  = Column(String(50),  nullable=False)
    # cột riêng của từng lớp con, nullable ở cấp DB vì không phải lớp nào cũng dùng
    brand         = Column(String(255), nullable=True)   # chỉ PaintingProduct dùng
    wood_source   = Column(String(255), nullable=True)   # chỉ WoodProduct dùng
    # relationship with InvoiceDetail model
    invoice_details = relationship("InvoiceDetail", back_populates="product")

    __mapper_args__ = {
        "polymorphic_on":       product_type,
        "polymorphic_identity": "generic",
    }
# lớp con tên hãng sơn  , thêm thuộc tính brand (tên hãng sơn)
class PaintingProduct(Product):
    __mapper_args__ = {
        "polymorphic_identity": "painting",
    }
# lớp con sản phẩm gỗ, thêm thuộc tính wood_source (nguồn nhập hàng)
class WoodProduct(Product):
    __mapper_args__ = {
        "polymorphic_identity": "wood",
    }