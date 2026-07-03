from pydantic import BaseModel
from datetime import datetime
# tạo ra các lớp cơ sở dữ liệu (schemas) cho mô hình Product. Các lớp này được sử dụng để xác định cấu trúc dữ liệu và xác thực dữ liệu đầu vào/đầu ra trong ứng dụng FastAPI.
class ProductBase(BaseModel):
    name: str
    code: str
    unit: str
    import_price: float
    selling_price: float
    stock: int = 0

# dùng khi tạo mới sản phẩm thông thường, ta sẽ kế thừa từ ProductBase và không cần thêm gì cả
class ProductCreate(ProductBase):
    """
    Schema for creating a new generic product."""
    pass

# dùng khi tạo mới sản phẩm sơn, ta sẽ kế thừa từ ProductBase và thêm trường brand
class PaintingProductCreate(ProductBase):
    """
    Schema for creating a new painting product."""
    brand: str

# dùng khi tạo mới sản phẩm gỗ, ta sẽ kế thừa từ ProductBase và thêm trường wood_source
class WoodProductCreate(ProductBase):
    """
    Schema for creating a new wood product."""
    wood_source: str

# dùng khi update sản phẩm, ta sẽ kế thừa từ BaseModel và có thể update bất kỳ trường nào trong ProductBase
class ProductUpdate(BaseModel):
    """
    Schema for updating an existing product."""
    name: str | None = None
    unit: str | None = None
    import_price: float | None = None
    selling_price: float | None = None
    stock: int | None = None
    brand: str | None = None
    wood_source: str | None = None

# thêm id, import_date, product_type, brand, wood_source và bật ORM mode
class ProductInDBBase(ProductBase):
    id: int
    import_date: datetime | None = None
    product_type: str
    brand: str | None = None
    wood_source: str | None = None

    class Config:
        from_attributes = True # pythantic sẽ sử dụng chế độ ORM để ánh xạ dữ liệu từ các đối tượng SQLAlchemy sang các đối tượng Pydantic.

class Product(ProductInDBBase):
    """
    Schema return for client."""
    pass