from flask import Flask, render_template
from routes.goods import goods_bp
from routes.customers import customers_bp
from routes.invoices import invoices_bp
from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


# đăng ký các blueprint với ứng dụng chính 
app.register_blueprint(goods_bp, url_prefix='/goods')
app.register_blueprint(customers_bp, url_prefix='/customers')
app.register_blueprint(invoices_bp, url_prefix='/invoices')

# route cơ bản để kiểm tra ứng dụng hoạt động
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context(): 
        db.create_all() # tạo tất cả các bảng trong cơ sở dữ liệu nếu chưa tồn tại
    app.run(debug=True)