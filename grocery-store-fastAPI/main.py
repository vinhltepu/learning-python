from fastapi import FastAPI
from fastapi import Request
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

@app.get("/")
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )
