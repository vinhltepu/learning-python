from sqlalchemy import Column, Integer, String ,Text, ForeignKey,DateTime
from sqlalchemy.orm import func
from sqlalchemy.orm import relationship

from app.db.base import Base
# Đây là model Book, đại diện cho bảng books trong database, có các trường id, title, description, publisher_year, author_id, category_id, cover_image, created_at, updated_at và mối quan hệ với bảng authors và categories thông qua relationship.
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    publisher_year  = Column(Integer, nullable=True)
    # tạo các khóa ngoại để liên kết với bảng authors và categories, với ondelete="RESTRICT" để ngăn chặn việc xóa tác giả hoặc danh mục nếu có sách liên quan
    author_id = Column(Integer, ForeignKey("authors.id"), ondelete="RESTRICT", nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), ondelete="RESTRICT", nullable=False)
    # lưu đuờng dẫn đến hình ảnh bìa sách, có thể null nếu không có hình ảnh
    cover_image = Column(String(255), nullable=True)
    # tự động ghi thời gian tạo và cập nhật bản ghi, sử dụng func.now() để lấy thời gian hiện tại từ cơ sở dữ liệu
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # relationship with Author model
    author = relationship("Author", back_populates="books")
    
    # relationship with Category model
    category = relationship("Category", back_populates="books")
