from typing import Generator
from fastapi import Depends, Header, HTTPException
from fastapi.templating import Jinja2Templates
from app.db.session import SessionLocal
from app.core.security import decode_token


# kết nối với databasse
def get_db() -> Generator:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# khai báo templates đ
templates = Jinja2Templates(directory="app/templates")


# lấy thong tin user hiện tại từ access token
def get_current_user(
    authorization: str = Header(...)
):

    # lấy thông tin từ token
    token = authorization.replace("Bearer ", "")

    # giải mã token
    payload = decode_token(token)

    return payload


# chỉ Admin được sử dụng
def admin_required(
    current_user: dict = Depends(get_current_user)
):

    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="chỉ Admin mới được phép chỉnh sửa"
        )

    return current_user


# Admin và Manager được sử dụng
def manager_required(
    current_user: dict = Depends(get_current_user)
):

    if current_user["role"] not in ["admin", "manager"]:
        raise HTTPException(
            status_code=403,
            detail="bạn không có quyền"
        )

    return current_user


# Admin, Manager và Staff đều được sử dụng
def staff_required(
    current_user: dict = Depends(get_current_user)
):

    if current_user["role"] not in ["admin", "manager", "staff"]:
        raise HTTPException(
            status_code=403,
            detail="bạn không có quyền"
        )

    return current_user