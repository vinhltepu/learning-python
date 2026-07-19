from fastapi import APIRouter, Depends, HTTPException, status, Query , Request , Form
from fastapi.responses import RedirectResponse
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.api.deps import get_db , templates
from app import models
from app.schemas.product import Product, ProductCreate, PaintingProductCreate, WoodProductCreate, ProductUpdate

router = APIRouter()

@router.get("/", response_model=List[Product])
def list_products(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    product_type: str | None = Query(None),
    keyword: str | None = Query(None),
    low_stock: bool = Query(False),
):
    """List products with optional filters"""
    mp = models.Product
    query = db.query(mp)
    if product_type is not None:
        query = query.filter(mp.product_type == product_type)

    if keyword is not None:
        like_pattern = f"%{keyword}%"
        query = query.filter(
            or_(
                mp.name.ilike(like_pattern),
                mp.code.ilike(like_pattern),
            )
        )
    if low_stock:
        query = query.filter(mp.stock < 10)

    products = query.offset(skip).limit(limit).all()
    return products


@router.get("/{product_id}", response_model=Product)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
    ):
    """Get product detail according id"""
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    
    return product
# create product
@router.post("/generic", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_generic_product(
    product_in: ProductCreate,
    db: Session = Depends(get_db)
    ):
    existing = db.query(models.Product).filter(models.Product.code == product_in.code).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this code already exists",
        )
    # dùng models.Product để tạo sản phẩm thông thường
    product = models.Product(
        name = product_in.name,
        code = product_in.code,
        unit = product_in.unit,
        import_price = product_in.import_price,
        selling_price = product_in.selling_price,
        stock = product_in.stock,
        product_type = "generic",
        )
    
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
# create painting product
@router.post("/painting", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_painting_product(
    product_in: PaintingProductCreate,
    db: Session = Depends(get_db)
    ):
    existing = db.query(models.Product).filter(models.Product.code == product_in.code).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this code already exists",
        )
    # dùng models.PaintingProduct để tạo sản phẩm sơn, vì nó có thêm trường brand
    product = models.PaintingProduct(
        name = product_in.name,
        code = product_in.code,
        unit = product_in.unit,
        import_price = product_in.import_price,
        selling_price = product_in.selling_price,
        stock = product_in.stock,
        product_type = "painting",
        brand = product_in.brand,
        )
    
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
# create wood product
@router.post("/wood", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_wood_product(
    product_in: WoodProductCreate,
    db: Session = Depends(get_db)
    ):
    existing = db.query(models.Product).filter(models.Product.code == product_in.code).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this code already exists",
        )
    # dùng models.WoodProduct để tạo sản phẩm gỗ, vì nó có thêm trường wood_source
    product = models.WoodProduct(
        name = product_in.name,
        code = product_in.code,
        unit = product_in.unit,
        import_price = product_in.import_price,
        selling_price = product_in.selling_price,
        stock = product_in.stock,
        product_type = "wood",
        wood_source = product_in.wood_source,
        )
    
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
# update product 
@router.put("/{product_id}", response_model=Product)
def update_product(
    product_id: int,
    product_up: ProductUpdate,
    db: Session = Depends(get_db)
    ):
    # cái này là để lấy sản phẩm theo id, nếu không có thì raise 404
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    # update các field nếu có trong product_up
    if product_up.name is not None:
        product.name = product_up.name
    if product_up.unit is not None:
        product.unit = product_up.unit
    if product_up.import_price is not None:
        product.import_price = product_up.import_price
    if product_up.selling_price is not None:
        product.selling_price = product_up.selling_price
    if product_up.stock is not None:
        product.stock = product_up.stock
    if product_up.brand is not None:
        product.brand = product_up.brand
    if product_up.wood_source is not None:
        product.wood_source = product_up.wood_source
    
    db.commit()
    db.refresh(product)
    return product
# delete product
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
    ):
    # lấy sản phẩm theo id, nếu không có thì raise 404
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    
    db.delete(product)
    db.commit()

@router.get("/edit/{product_id}", include_in_schema=False)
def edit_product_page(product_id: int, request: Request, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    return templates.TemplateResponse(
    request=request,
    name="product_edit.html",
    context={
        "product": product
        }
    )

@router.post("/edit/{product_id}", include_in_schema=False)
def edit_product_submit(
    product_id: int,
    name: str = Form(...),
    unit: str = Form(...),
    import_price: float = Form(...),
    selling_price: float = Form(...),
    stock: int = Form(...),
    db: Session = Depends(get_db),
):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    product.name = name
    product.unit = unit
    product.import_price = import_price
    product.selling_price = selling_price
    product.stock = stock
    db.commit()
    return RedirectResponse(url="/products-page", status_code=303)

@router.get("/delete/{product_id}", include_in_schema=False)
def delete_product_page(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    db.delete(product)
    db.commit()
    return RedirectResponse(url="/products-page", status_code=303)

@router.get("/products-page", include_in_schema=False)
def products_page(
    request: Request,
    db: Session =Depends(get_db)
):
    products = db.query(models.Product).all()

    return templates.TemplateResponse(
        request=request,
        name="products.html",
        context={
            "products": products
        }
    )