from pydantic import BaseModel
from datetime import datetime

from app.schemas.category import Category
from app.schemas.author import Author

class BookBase(BaseModel):
    title: str
    description: str
    publisher_year: int 
    author_id: int
    category_id: int

class BookCreate(BookBase):
    """
    Schema for creating a new Book."""
    pass

class BookUpdate(BaseModel):
    """
    Schema for updating an existing Book."""
    title: str | None = None
    description: str | None = None
    publisher_year: int | None = None
    author_id: int | None = None
    category_id: int | None = None

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
   author: Author
   category: Category

