from flask import Blueprint, request, jsonify
from models.invoices import Invoice

# tạo blueprint cho các route liên quan đến hóa đơn
invoices_bp = Blueprint('invoices', __name__)


