from flask import Blueprint, request, jsonify 
from models.goods import Goods

# tạo blueprint cho các route liên quan đến hàng hóa
goods_bp = Blueprint('goods', __name__)

