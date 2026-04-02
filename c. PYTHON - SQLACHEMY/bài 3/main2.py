from models import engine, Product 
from sqlalchemy.orm import Session 

session = Session(bind=engine)

products = session.query(Product).order_by(Product.price).all() # Sắp xếp sản phẩm theo giá tăng dần
# session.query(Product).order_by(Product.price.desc()).all() # Sắp xếp sản phẩm theo giá giảm dần
# session.query(Product).order_by(Product.name).all() # Sắp xếp sản phẩm theo tên tăng dần
# session.query(Product).order_by(Product.name.desc()).all() # Sắp xếp sản phẩm theo tên giảm dần

for product in products:
    print(f"Product Name: {product.name}, Price: {product.price}")

session.close()