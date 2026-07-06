from pydantic import BaseModel
# tạo ra các lớp cơ sở dữ liệu (schemas) cho mô hình Customer. Các lớp này được sử dụng để xác định cấu trúc dữ liệu và xác thực dữ liệu đầu vào/đầu ra trong ứng dụng FastAPI.
class CustomerBase(BaseModel):
    name: str
    phone: str
    address: str | None = None

class CustomerCreate(CustomerBase):
    pass

# dùng khi update khách hàng, ta sẽ kế thừa từ BaseModel và có thể update bất kỳ trường nào trong CustomerBase
class CustomerUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    address: str | None = None

# thêm id, total_spent, customer_type, discount_rate và bật ORM mode
class CustomerInDBBase(CustomerBase):
    id: int
    total_spent: float
    customer_type: str
    discount_rate: float = 0.0

    class Config:
        from_attributes = True # pythantic sẽ sử dụng chế độ ORM để ánh xạ dữ liệu từ các đối tượng SQLAlchemy sang các đối tượng Pydantic.

class CustomerOut(CustomerInDBBase):
    pass
class Customer(CustomerInDBBase):
    pass