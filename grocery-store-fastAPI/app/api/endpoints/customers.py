from fastapi import APIRouter, Depends, HTTPException, status, Query ,Request , Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional,Literal

from app.api.deps import get_db , templates
from app import models
from app.schemas.customer import  CustomerOut, CustomerUpdate , CustomerCreate



router = APIRouter()

# danh sách khách hàng, có thể tìm kiếm theo tên hoặc số điện thoại, phân trang bằng skip và limit
@router.get("/", response_model=List[CustomerOut])
def list_customers(
    skip    : int = 0,
    limit   : int = 100,
    keyword : Optional[str] = Query(None, description="Tìm theo tên hoặc SĐT"),
    db      : Session = Depends(get_db),
):
    query = db.query(models.Customer)
    if keyword:
        like = f"%{keyword}%"
        query = query.filter(or_(
            models.Customer.name.ilike(like),
            models.Customer.phone.ilike(like),
        )) 
    return query.offset(skip).limit(limit).all()
@router.get("/edit/{customer_id}", include_in_schema=False)
def edit_customer_page(
    customer_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    customer = _get_or_404(customer_id, db)

    customers = db.query(models.Customer).all()

    return templates.TemplateResponse(
        "customers.html",
        {
            "request": request,
            "customers": customers,
            "customer": customer
        }
    )

@router.get("/delete/{customer_id}", include_in_schema=False)
def delete_customer_page(customer_id: int, db: Session = Depends(get_db)):
    customer = _get_or_404(customer_id, db)
    invoices = db.query(models.Invoice).filter(models.Invoice.customer_id == customer_id).all()
    if invoices:
        return RedirectResponse(url="/customers-page", status_code=303)  # có hóa đơn thì không xóa
    db.delete(customer)
    db.commit()
    return RedirectResponse(url="/customers-page", status_code=303)

# hiển thị khách hàng theo id, nếu không có thì trả về 404
@router.get("/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return _get_or_404(customer_id, db)

# tạo mới khách hàng, kiểm tra số điện thoại có trùng không
@router.post("/", response_model=CustomerOut, status_code=status.HTTP_201_CREATED)
def create_customer(
    data: CustomerCreate,
    customer_type: Literal["regular", "vip"] = Query(..., description="Loại khách hàng"),
    db: Session = Depends(get_db),
):
    _check_phone_unique(data.phone, db)
    model_cls = models.VIPCustomer if customer_type == "vip" else models.RegularCustomer
    customer = model_cls(**data.model_dump())
    db.add(customer); db.commit(); db.refresh(customer)
    return customer

# cập nhật thông tin khách hàng
@router.put("/{customer_id}", response_model=CustomerOut)
def update_customer(customer_id: int, data: CustomerUpdate, db: Session = Depends(get_db)):
    customer = _get_or_404(customer_id, db)

    if data.phone and data.phone != customer.phone:
        _check_phone_unique(data.phone, db)

    for field, value in data.model_dump(exclude_none=True).items():
        setattr(customer, field, value)

    db.commit(); db.refresh(customer)
    return customer


def _get_or_404(customer_id: int, db: Session):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Khách hàng không tồn tại")
    return customer

# xóa khách hàng , nếu khách hàng có hóa đơn thì không cho xóa
@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = _get_or_404(customer_id, db)
    # Kiểm tra xem khách hàng có hóa đơn nào không
    invoices = db.query(models.Invoice).filter(models.Invoice.customer_id == customer_id).all()
    if invoices:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Khách hàng đã có hóa đơn, không thể xóa")
    db.delete(customer); db.commit()


def _check_phone_unique(phone: str, db: Session):
    existing = db.query(models.Customer).filter(models.Customer.phone == phone).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Số điện thoại đã tồn tại")

