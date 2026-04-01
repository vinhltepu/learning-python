from flask import Flask
from blueprints.user.routes import user_bp # import blueprint user từ file routes.py trong thư mục user
from blueprints.admin.routes import admin_bp # import blueprint admin từ file routes.py trong thư mục admin
 
app = Flask(__name__)
app.register_blueprint(user_bp) # đăng ký blueprint user vào app chính
app.register_blueprint(admin_bp) # đăng ký blueprint admin vào app chính


@app.route('/')
def index():
    return '<h1>Xin chào các bạn</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=8888) 

# cần một cái route dành riêng cho user
# cần một cái route dành riêng cho api 
# cần một cái route dành riêng cho admin