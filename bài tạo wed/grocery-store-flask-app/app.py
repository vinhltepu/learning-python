from flask import Flask
from routes.goods import goods_bp
from routes.customers import customers_bp
from routes.invoices import invoices_bp

app = Flask(__name__)

# đăng ký các blueprint với ứng dụng chính 
app.register_blueprint(goods_bp, url_prefix='/goods')
app.register_blueprint(customers_bp, url_prefix='/customers')
app.register_blueprint(invoices_bp, url_prefix='/invoices')

# route cơ bản để kiểm tra ứng dụng hoạt động
@app.route('/')
def index():
    return "Welcome to the Grocery Store Management System"

if __name__ == '__main__':
    app.run(debug=True)