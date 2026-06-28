from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.product import Product, PaintingProduct, WoodProduct
from app.models.customer import Customer, RegularCustomer, VIPCustomer
from app.models.invoice import Invoice, InvoiceDetail