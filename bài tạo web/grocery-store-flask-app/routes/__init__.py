from flask import Blueprint # import Blueprint để tạo nhóm route

# tạo blueprint để tổ chức các route
routes_bp = Blueprint('routes', __name__)

# import các module route từ thư mục hiện tại
from . import goods, customers, invoices

routes_bp.register_blueprint(goods.goods_bp) # đăng ký blueprint cho routes liên quan đến hàng hóa
routes_bp.register_blueprint(customers.customers_bp) # đăng ký blueprint cho routes liên quan
routes_bp.register_blueprint(invoices.invoices_bp) # đăng ký blueprint cho routes liên quan đến hóa đơn
