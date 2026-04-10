from flask import Blueprint, request, jsonify # import Blueprint để tạo nhóm route, request để xử lý dữ liệu từ client, jsonify để trả về dữ liệu dạng JSON
from models.customers import Customer # import model Customer để tương tác với bảng customers trong cơ sở dữ liệu

# tạo blueprint cho các route liên quan đến khách hàng
customers_bp = Blueprint('customers', __name__)

