
# Khởi tạo package models và import các module cần thiết
from .goods import Product, PaintingProduct, WoodProduct
from .customers import Customer, RegularCustomer, VIPCustomer
from .invoices import Invoice, InvoiceDetail

__all__ = ['Goods', 'Customers', 'Invoices']