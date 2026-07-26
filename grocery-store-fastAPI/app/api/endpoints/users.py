from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db, templates, admin_required
from app import models
from app.schemas.user import User, UserCreate, UserUpdate


router = APIRouter()


## danh sách user (API) với quyền admin
@router.get(
    "/",
    response_model=List[User],
    dependencies=[Depends(admin_required)]
)
def list_users(
    db: Session = Depends(get_db)
):
    return db.query(models.User).all()

# danh sách user (trang web)
@router.get("/users-page", include_in_schema=False)
def users_page(
    request: Request,
    db: Session = Depends(get_db)
):

    users = db.query(models.User).all()

    return templates.TemplateResponse(
        request=request,
        name="users.html",
        context={
            "users": users
        }
    )

# trang thêm user
@router.get("/add", include_in_schema=False)
def add_user_page(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="user_add.html",
        context={}
    )

# thêm user (trang web)
@router.post("/add", include_in_schema=False)
def add_user(

    username: str = Form(...),
    password: str = Form(...),
    full_name: str = Form(...),
    role: str = Form(...),

    db: Session = Depends(get_db)

):

    existing = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Tên đăng nhập đã tồn tại"
        )

    user = models.User(
        username=username,
        password=password,
        full_name=full_name,
        role=role
    )

    db.add(user)
    db.commit()

    return RedirectResponse(
        url="/users-page",
        status_code=303
    )

# lấy thông tin user theo ID (API)
@router.get(
    "/{user_id}",
    response_model=User,
    dependencies=[Depends(admin_required)]
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

# tạo user mới (API)
@router.post(
    "/",
    response_model=User,
    dependencies=[Depends(admin_required)]
)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(models.User).filter(
        models.User.username == data.username
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Tên đăng nhập đã tồn tại"
        )

    user = models.User(
        username=data.username,
        password=data.password,
        full_name=data.full_name,
        role=data.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

# sửa user (API)
@router.put(
    "/{user_id}",
    response_model=User,
    dependencies=[Depends(admin_required)]
)
def update_user(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    for field, value in data.model_dump(
        exclude_none=True
    ).items():

        setattr(user, field, value)

    db.commit()
    db.refresh(user)

    return user


# sửa user (trang web)
@router.get(
    "/edit/{user_id}",
    include_in_schema=False
)
def edit_user_page(

    user_id: int,
    request: Request,
    db: Session = Depends(get_db)

):

    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    return templates.TemplateResponse(
        request=request,
        name="user_edit.html",
        context={
            "user": user
        }
    )


# sửa user (trang web)
@router.post(
    "/edit/{user_id}",
    include_in_schema=False
)
def edit_user(

    user_id: int,

    username: str = Form(...),
    password: str = Form(...),
    full_name: str = Form(...),
    role: str = Form(...),

    db: Session = Depends(get_db)

):

    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    user.username = username
    user.password = password
    user.full_name = full_name
    user.role = role

    db.commit()

    return RedirectResponse(
        url="/users-page",
        status_code=303
    )

# xóa user (API)
@router.delete(
    "/{user_id}",
    dependencies=[Depends(admin_required)]
)
def delete_user(

    user_id: int,
    db: Session = Depends(get_db)

):

    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "Delete successfully"
    }

# xóa user (trang web)
@router.get(
    "/delete/{user_id}",
    include_in_schema=False
)
def delete_user_page(

    user_id: int,
    db: Session = Depends(get_db)

):

    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()


    db.delete(user)
    db.commit()

    return RedirectResponse(
        url="/users-page",
        status_code=303
    )