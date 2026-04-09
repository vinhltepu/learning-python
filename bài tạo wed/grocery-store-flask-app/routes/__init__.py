from flask import Blueprint

# tạo blueprint để tổ chức các route
routes_bp = Blueprint('routes', __name__)

# import các module route từ thư mục hiện tại
from . import goods, customers, invoices