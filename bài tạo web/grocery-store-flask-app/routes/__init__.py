from flask import Blueprint # import Blueprint để tạo nhóm route

# tạo blueprint để tổ chức các route
routes_bp = Blueprint('routes', __name__)

# import các module route từ thư mục hiện tại
from . import goods, customers, invoices