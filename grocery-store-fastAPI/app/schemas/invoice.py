from pydantic import BaseModel
from datetime import datetime

from app.schemas.product import Product
from app.schemas.customer import Customer
# tạo ra các lớp cơ sở dữ liệu (schemas) cho mô hình InvoiceDetail. Các lớp này được sử dụng để xác định cấu trúc dữ liệu và xác thực dữ liệu đầu vào/đầu ra trong ứng dụng FastAPI.
class InvoiceDetailBase(BaseModel):
    product_id: int
    quantity: int

# dùng khi tạo mới 1 dòng chi tiết hóa đơn, ta sẽ kế thừa từ InvoiceDetailBase và không cần thêm gì cả
class InvoiceDetailCreate(InvoiceDetailBase):
    pass

# thêm id, invoice_id, unit_price, subtotal và bật ORM mode
class InvoiceDetailInDBBase(InvoiceDetailBase):
    id: int
    invoice_id: int
    unit_price: float
    subtotal: float
    product: Product # trả cả object product lồng bên trong object invoice detail

    class Config:
        from_attributes = True # pythantic sẽ sử dụng chế độ ORM để ánh xạ dữ liệu từ các đối tượng SQLAlchemy sang các đối tượng Pydantic.

class InvoiceDetail(InvoiceDetailInDBBase):
    pass

# tạo ra các lớp cơ sở dữ liệu (schemas) cho mô hình Invoice
class InvoiceBase(BaseModel):
    customer_id: int

# dùng khi tạo mới 1 hóa đơn, ta sẽ kế thừa từ InvoiceBase và thêm danh sách items
class InvoiceCreate(InvoiceBase):
    items: list[InvoiceDetailCreate]

# thêm id, created_at, total_amount, discount_rate, final_amount và bật ORM mode
class InvoiceInDBBase(InvoiceBase):
    id: int
    created_at: datetime | None = None
    total_amount: float
    discount_rate: float
    final_amount: float

    class Config:
        from_attributes = True # pythantic sẽ sử dụng chế độ ORM để ánh xạ dữ liệu từ các đối tượng SQLAlchemy sang các đối tượng Pydantic.

# schema nested for customer and invoice details
class Invoice(InvoiceInDBBase):
    customer: Customer # trả cả object customer lồng bên trong object invoice
    details: list[InvoiceDetail] = [] # trả cả danh sách chi tiết hóa đơn lồng bên trong object invoice