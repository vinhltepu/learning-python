from flask import Blueprint, request, jsonify
from models.customers import Customer

# tạo blueprint cho các route liên quan đến khách hàng
customers_bp = Blueprint('customers', __name__)

