from fastapi import APIRouter, Depends, HTTPException, Header, Request , Form
from sqlalchemy.orm import Session

from app.api.deps import get_db , templates
from app import models
from fastapi.responses import RedirectResponse
from app.schemas.user import UserLogin, Token, RefreshToken
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password
)

router = APIRouter()
# mở trang đăng nhập
@router.get("/login-page", include_in_schema=False)
def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )

# xử lý đăng nhập 
@router.post("/login-page", include_in_schema=False)
def login_page(

    username: str = Form(...),
    password: str = Form(...),

    db: Session = Depends(get_db)

):

    db_user = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Tên đăng nhập không đúng"
        )

    if not verify_password(password, db_user.password):
        raise HTTPException(
            status_code=400,
            detail="Mật khẩu không đúng"
        )
# tạo JWT
    # Tạo Access Token
    access_token = create_access_token(
        {
            "sub": db_user.username,
            "role": db_user.role
        }
    )

    # Tạo Refresh Token
    refresh_token = create_refresh_token(
        {
            "sub": db_user.username
        }
    )
# chuyển người dùng đến trang phù hợp với vai trò của họ
    if db_user.role == "admin":

        return RedirectResponse(
            url="/admin",
            status_code=303
        )

    elif db_user.role == "manager":

        return RedirectResponse(
            url="/manager",
            status_code=303
        )

    else:

        return RedirectResponse(
            url="/shop",
            status_code=303
        )

# API đăng nhập, trả về access token và refresh token
@router.post("/login", response_model=Token)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Tên đăng nhập không đúng"
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=400,
            detail="Mật khẩu không đúng"
        )

    access_token = create_access_token(
        {
            "sub": db_user.username,
            "role": db_user.role
        }
    )

    refresh_token = create_refresh_token(
        {
            "sub": db_user.username
        }
    )

    return Token(
        access_token=access_token,
        refresh_token=refresh_token
    )

# trang đăng ký
@router.get("/register-page", include_in_schema=False)
def register_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={}
    )

# xử lý đăng kí xem có trùng thông tin không
@router.post("/register-page", include_in_schema=False)
def register(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    full_name: str = Form(...),
    db: Session = Depends(get_db)
):

    # kiểm tra username đã tồn tại chưa
    user = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if user:
        return templates.TemplateResponse(
            request=request,
            name="register.html",
            context={
                "error": "Tên đăng nhập đã tồn tại"
            }
        )

    # tạo tài khoản mới
    new_user = models.User(
        username=username,
        password=hash_password(password),
        full_name=full_name,
        role="staff"
    )

    # lưu vào database
    db.add(new_user)
    db.commit()

    # đăng ký thành công, chuyển hướng về trang đăng nhập
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={
            "success": "Tạo tài khoản thành công!"
        }
    )
# refresh token
@router.post("/refresh", response_model=Token)
def refresh(
    token: RefreshToken,
    db: Session = Depends(get_db)
):

    payload = decode_token(token.refresh_token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Refresh Token không hợp lệ"
        )

    username = payload["sub"]

    user = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User không tồn tại"
        )

    access_token = create_access_token(
        {
            "sub": user.username,
            "role": user.role
        }
    )

    refresh_token = create_refresh_token(
        {
            "sub": user.username
        }
    )

    return Token(
        access_token=access_token,
        refresh_token=refresh_token
    )

# đăng xuất (chỉ xóa token ở phía client, server không lưu token)
@router.post("/logout")
def logout():

    return {
        "message": "Đăng xuất thành công"
    }


# thông tin user hiện tại
@router.get("/me")
def me(
    authorization: str = Header(...)
):

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Token không hợp lệ"
        )

    token = authorization.replace("Bearer ", "")

    payload = decode_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Token hết hạn hoặc không hợp lệ"
        )

    return payload