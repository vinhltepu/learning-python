from pydantic import BaseModel
from datetime import datetime

from app.schemas.category import Category
from app.schemas.author import Author
# tạo ra các lớp cơ sở dữ liệu (schemas) cho mô hình Book. Các lớp này được sử dụng để xác định cấu trúc dữ liệu và xác thực dữ liệu đầu vào/đầu ra trong ứng dụng FastAPI.
class BookBase(BaseModel):
    title: str
    description: str
    publisher_year: int 
    author_id: int
    category_id: int
# dùng khi tao mới 1 book, ta sẽ kế thừa từ BookBase và không cần thêm gì cả
class BookCreate(BookBase):
    """
    Schema for creating a new Book."""
    pass
# dùng khi update 1 book, ta sẽ kế thừa từ BaseModel và có thể update bất kỳ trường nào trong BookBase
class BookUpdate(BaseModel):
    """
    Schema for updating an existing Book."""
    title: str | None = None
    description: str | None = None
    publisher_year: int | None = None
    author_id: int | None = None
    category_id: int | None = None
# thêm id và bật ORM mode 
class BookInDBBase(BookBase):
    id: int
    title: str
    description: str
    publisher_year: int
    author_id: int
    category_id: int
    created_at: datetime
    updated_at: datetime
    cover_image: str | None = None
    
    class Config:
        from_attributes = True # pythantic sẽ sử dụng chế độ ORM để ánh xạ dữ liệu từ các đối tượng SQLAlchemy sang các đối tượng Pydantic.

# schema nested for author and category
class Book(BookInDBBase):
   author: Author # trả cả object author lồng bên trong object book
   category: Category # trả cả object category lồng bên trong object book

