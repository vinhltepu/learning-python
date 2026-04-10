from flask import Flask # import Flask để tạo ứng dụng web
from routes.goods import goods_bp # import blueprint cho routes liên quan đến hàng hóa
from routes.customers import customers_bp # import blueprint cho routes liên quan đến khách hàng
from routes.invoices import invoices_bp # import blueprint cho routes liên quan đến hóa đơn 
from config import Config # import cấu hình từ file config.py
from flask_sqlalchemy import SQLAlchemy # import SQLAlchemy để tương tác với cơ sở dữ liệu



app =Flask(__name__)
app.config.from_object(Config) # tải cấu hình từ class Config trong file config.py
db = SQLAlchemy(app) # khởi tạo SQLAlchemy với ứng dụng Flask


# đăng ký các blueprint với ứng dụng chính 
app.register_blueprint(goods_bp, url_prefix='/goods')
app.register_blueprint(customers_bp, url_prefix='/customers')
app.register_blueprint(invoices_bp, url_prefix='/invoices')

# route cơ bản để kiểm tra ứng dụng hoạt động
@app.route('/')
def index():
    return "Welcome to Quang Thuy Grocery Store "

if __name__ == '__main__':
    with app.app_context(): 
        db.create_all() # tạo tất cả các bảng trong cơ sở dữ liệu nếu chưa tồn tại
    app.run(debug=True)