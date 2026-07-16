from fastapi import FastAPI , Request, Depends 
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models 
from app.api.deps import get_db
from app.core.config import settings
from app.db.session import engine
from app.db import base  #kích hoạt import models để create_all biết bảng nào cần tạo
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import products, customers, invoices, stats

# Tạo tất cả các bảng trong cơ sở dữ liệu nếu chưa tồn tại
base.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,                                        
    description="API quản lý cửa hàng tạp hóa ngành mộc Quang Thúy",  
    version="1.0.0",                                                     
)
# khai báo thư mục static và templates để FastAPI có thể phục vụ các file tĩnh và template HTML
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(products.router,  prefix="/products",  tags=["Products"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(invoices.router,  prefix="/invoices",  tags=["Invoices"])
app.include_router(stats.router,     prefix="/stats",     tags=["Stats"])

@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    ) 


@app.get("/products-page", include_in_schema=False)
def products_page(request: Request, db: Session = Depends(get_db)):
    products_list = db.query(models.Product).all()
    return templates.TemplateResponse(
        request=request,
        name="products.html",
        context={"request": request, "products": products_list}  
    )


@app.get("/customers-page", include_in_schema=False)
def customers_page(request: Request, db: Session = Depends(get_db)):
    customers_list = db.query(models.Customer).all()
    return templates.TemplateResponse(
        request=request,
        name="customers.html",
        context={"request": request, "customers": customers_list, "customer": None}
    )


@app.get("/invoices-page", include_in_schema=False)
def invoices_page(request: Request, db: Session = Depends(get_db)):
    invoices_list = db.query(models.Invoice).all()
    return templates.TemplateResponse(
        request=request,
        name="invoices.html",
        context={"request": request, "invoices": invoices_list}
    )


@app.get("/stats-page", include_in_schema=False)
def stats_page(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        request=request,
        name="stats.html",
        context={
            "total_products": db.query(models.Product).count(),
            "total_customers": db.query(models.Customer).count(),
            "total_invoices": db.query(models.Invoice).count(),
            "total_revenue": db.query(func.sum(models.Invoice.final_amount)).scalar() or 0
        }
    )


    

