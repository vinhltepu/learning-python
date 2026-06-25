from pydantic import BaseModel
# tạo ra các lớp cơ sở dữ liệu (schemas) cho mô hình Author. Các lớp này được sử dụng để xác định cấu trúc dữ liệu và xác thực dữ liệu đầu vào/đầu ra trong ứng dụng FastAPI.
class AuthorBase(BaseModel):
    name: str
    bio: str | None = None

class AuthorCreate(AuthorBase):
    """
    Schema for creating a new author."""
    pass

class AuthorUpdate(BaseModel):
    """
    Schema for updating an existing author."""
    name: str | None = None
    bio: str | None = None

class AuthorInDBBase(AuthorBase):
    id: int

    class Config:
        from_attributes = True # pythantic sẽ sử dụng chế độ ORM để ánh xạ dữ liệu từ các đối tượng SQLAlchemy sang các đối tượng Pydantic.

class Author(AuthorInDBBase):
    """
    Schema return for client."""
    pass