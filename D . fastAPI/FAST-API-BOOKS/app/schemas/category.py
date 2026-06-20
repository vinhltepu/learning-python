from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    description: str | None = None

class CategoryCreate(CategoryBase):
    """
    Schema for creating a new category."""
    pass

class CategoryUpdate(BaseModel):
    """
    Schema for updating an existing category."""
    name: str | None = None
    description: str | None = None

class CategoryInDBBase(CategoryBase):
    id: int

    class Config:
        orm_mode = True # pythantic sẽ sử dụng chế độ ORM để ánh xạ dữ liệu từ các đối tượng SQLAlchemy sang các đối tượng Pydantic.

class Category(CategoryInDBBase):
    """
    Schema return for client."""
    pass
