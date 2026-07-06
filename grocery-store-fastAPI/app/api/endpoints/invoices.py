from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app import models
from app.schemas.invoice import Invoice, InvoiceCreate

router = APIRouter()

@router.get("/", response_model=List[Invoice])
def list_invoices(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    customer_id: int | None = Query(None),
):
    # Lấy danh sách hóa đơn với các điều kiện lọc
    query = db.query(models.Invoice)
    if customer_id is not None:
        query = query.filter(models.Invoice.customer_id == customer_id)

    invoices = query.offset(skip).limit(limit).all()
    return invoices


@router.get("/{invoice_id}", response_model=Invoice)
def get_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
    ):
    # Lấy chi tiết hóa đơn theo id
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found",
        )
    
    return invoice

@router.post("/", response_model=Invoice, status_code=status.HTTP_201_CREATED)
def create_invoice(
    invoice_in: InvoiceCreate,
    db: Session = Depends(get_db)
    ):
    # tạo hóa đơn mới, kiểm tra tồn tại của khách hàng và sản phẩm, đồng thời kiểm tra số lượng tồn kho của sản phẩm
    customer = db.query(models.Customer).filter(models.Customer.id == invoice_in.customer_id).first()
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer does not exist",
        )

    detail_rows = []
    total_amount = 0.0
    # kiểm tra từng sản phẩm trong hóa đơn, nếu sản phẩm không tồn tại hoặc số lượng tồn kho không đủ thì raise HTTPException
    for item in invoice_in.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product id {item.product_id} does not exist",
            )
        # nếu số lượng tồn kho của sản phẩm nhỏ hơn số lượng yêu cầu trong hóa đơn, thì raise HTTPException
        if product.stock < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product '{product.name}' not enough stock (remaining: {product.stock})",
            )
        subtotal = product.selling_price * item.quantity
        total_amount += subtotal
        detail_rows.append((product, item.quantity, product.selling_price, subtotal))

    # thêm logic tính toán giảm giá dựa trên tổng số tiền đã chi tiêu của khách hàng
    discount_rate = customer.get_discount_rate()
    final_amount = total_amount * (1 - discount_rate)
    # tạo hóa đơn và chi tiết hóa đơn, đồng thời cập nhật số lượng tồn kho của sản phẩm
    invoice = models.Invoice(
        customer_id = customer.id,
        total_amount = total_amount,
        discount_rate = discount_rate,
        final_amount = final_amount,
    )
    db.add(invoice)
    db.flush()  # flush để lấy invoice.id trước khi thêm chi tiết hóa đơn

    for product, qty, unit_price, subtotal in detail_rows:
        detail = models.InvoiceDetail(
            invoice_id = invoice.id,
            product_id = product.id,
            quantity = qty,
            unit_price = unit_price,
            subtotal = subtotal,
        )
        db.add(detail)
        product.stock -= qty

    # update customer's total_spent
    customer.total_spent += final_amount

    db.commit()
    db.refresh(invoice)
    return invoice
    
# tạo endpoint để xóa hóa đơn theo id, đồng thời cập nhật lại số lượng tồn kho của các sản phẩm trong hóa đơn
@router.delete("/{invoice_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
    ):
    # xóa hóa đơn theo id, nếu không có thì raise 404
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found",
        )
    
    db.delete(invoice)
    db.commit()
# chỉnh sửa hóa đơn bằng Patch, chỉ cho phép chỉnh sửa số lượng sản phẩm trong hóa đơn, đồng thời cập nhật lại số lượng tồn kho của các sản phẩm trong hóa đơn
@router.patch("/{invoice_id}", response_model=Invoice)
def update_invoice(
    invoice_id: int,
    invoice_in: InvoiceCreate,
    db: Session = Depends(get_db)
    ):
    # chỉnh sửa hóa đơn bằng Patch, chỉ cho phép chỉnh sửa số lượng sản phẩm trong hóa đơn, đồng thời cập nhật lại số lượng tồn kho của các sản phẩm trong hóa đơn
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found",
        )
