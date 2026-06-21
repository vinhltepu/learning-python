from pydantic import BaseModel

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