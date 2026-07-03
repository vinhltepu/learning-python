from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from typing import Optional

from app.api.deps import get_db
from app import models

router = APIRouter()

# Thống kê sản phẩm sắp hết hàng, lọc theo ngưỡng tồn kho
@router.get("/low-stock")
def low_stock_products(
    threshold: int = 10,
    db: Session = Depends(get_db)
):
    """List products with stock below threshold (default < 10)"""
    products = (
        db.query(models.Product)
        .filter(models.Product.stock < threshold)
        .order_by(models.Product.stock)
        .all()
    )
    return [
        {
            "id":    p.id,
            "name":  p.name,
            "code":  p.code,
            "stock": p.stock,
            "unit":  p.unit,
        }
        for p in products
    ]


# Thống kê doanh thu theo năm hoặc tháng cụ thể
@router.get("/revenue")
def revenue_by_period(
    year:  int           = Query(..., description="Năm cần thống kê"),
    month: Optional[int] = Query(None, description="Tháng cần thống kê, bỏ trống = cả năm"),
    db:    Session       = Depends(get_db)
):
    """Total revenue by year or specific month"""
    query = db.query(func.sum(models.Invoice.final_amount)).filter(
        extract("year", models.Invoice.created_at) == year
    )
    if month is not None:
        query = query.filter(
            extract("month", models.Invoice.created_at) == month
        )
    total = query.scalar() or 0.0
    return {"year": year, "month": month, "total_revenue": total}


# Thống kê top khách hàng mua nhiều nhất theo tổng tiền tích lũy
@router.get("/top-customers")
def top_customers(
    limit: int     = 5,
    db:    Session = Depends(get_db)
):
    """Top customers by total spent"""
    customers = (
        db.query(models.Customer)
        .order_by(models.Customer.total_spent.desc())
        .limit(limit)
        .all()
    )
    return [
        {
            "id":            c.id,
            "name":          c.name,
            "phone":         c.phone,
            "customer_type": c.customer_type,
            "total_spent":   c.total_spent,
            "discount_rate": c.get_discount_rate(),  # polymorphism: VIP tự tính đúng % giảm giá
        }
        for c in customers
    ]