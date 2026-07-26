from pydantic import BaseModel
from datetime import datetime

# Dùng để tạo tài khoản người dùng mới
class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str
    role: str = "staff"

# Dùng để update thông tin người dùng
class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    full_name: str | None = None
    role: str | None = None

# Dùng để xác thực thông tin đăng nhập của người dùng
class UserLogin(BaseModel):
    username: str
    password: str

# Dùng để trả về thông tin người dùng (không bao gồm mật khẩu)
class User(BaseModel):
    id: int
    username: str
    full_name: str
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

# Trả Access Token + Refresh Token
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
# Xin Access Token mới
class RefreshToken(BaseModel):
    refresh_token: str