from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine
from app.db import base  #kích hoạt import models để create_all biết bảng nào cần tạo

from app.api.endpoints import products, customers, invoices, stats

# Tạo tất cả các bảng trong cơ sở dữ liệu nếu chưa tồn tại
base.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,                                        
    description="API quản lý cửa hàng tạp hóa ngành mộc Quang Thúy",  
    version="1.0.0",                                                     
)

app.include_router(products.router,  prefix="/products",  tags=["Products"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(invoices.router,  prefix="/invoices",  tags=["Invoices"])
app.include_router(stats.router,     prefix="/stats",     tags=["Stats"])


@app.get("/")  
def read_root():
    return {"message": "Welcome to Quang Thuy Grocery Store API"}