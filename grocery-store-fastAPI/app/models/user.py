from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.db.base import Base

# tạo 1 class có thể dùng được cho cả 3 Admin , Manager , Staff vì cả ba đều có cùng thuộc tính.
class User(Base):
    __tablename__ = "users"

    # khóa chính
    id = Column(Integer, primary_key=True, index=True)

    # tên đăng nhập
    username = Column(String(50), unique=True, nullable=False, index=True)

    # mật khẩu 
    password = Column(String(255), nullable=False)

    # họ tên
    full_name = Column(String(100), nullable=False)

    # quyền của người dùng
    role = Column(String(20), nullable=False, default="staff")

    # tài khoản còn hoạt động hay không
    is_active = Column(Boolean, default=True)

    # ngày tạo tài khoản
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # refresh token để làm mới access token
    refresh_token = Column(String(255), nullable=True)  