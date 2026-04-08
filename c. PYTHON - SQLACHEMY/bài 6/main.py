from models import engine, Product
from sqlalchemy.orm import Session 

# in_ : dùng để kiểm tra các giá trị có thuộc một danh sách các giá trị hay không 
# is_ : dùng để kiểm tra xem một giá trị có phải là None hay không
# like : so sánh chuỗi phân biệt chữ hoa chữ thường
# ilike : so sánh chuỗi không phân biệt chữ hoa chữ thường
# pattern :
#+ % : đại diện cho bất kỳ chuỗi nào (bao gồm cả chuỗi rỗng)
#+ _ : đại diện cho một ký tự bất kỳ
session = Session(bind=engine)
if not session.query(Product).first():
    session.add_all([
        Product(name='Laptop', price=1500.0),
        Product(name='Smartphone', price=1200.0),
        Product(name='Tablet', price=900.0),
        Product(name='Headphones', price=250.0),
        Product(name='Smartwatch', price=1100.0)
    ])
    session.commit()

result = session.query(Product).filter(Product.name.in_(['Laptop', 'Smartphone'])).all() # truy vấn xem có bao nhiêu sản phẩm có tên là 'Laptop' hoặc 'Smartphone' trong bảng products.

query = session.query(Product).filter(Product.name.is_(None)).all() # truy vấn xem có bao nhiêu sản phẩm có tên là None trong bảng products.

like_query = session.query(Product).filter(Product.name.like('%Laptop%')).all() # truy vấn xem có bao nhiêu sản phẩm có tên chứa 'Laptop' trong bảng products.

ilike_query = session.query(Product).filter(Product.name.ilike('%laptop%')).all() # truy vấn xem có bao nhiêu sản phẩm có tên chứa 'laptop' (không phân biệt chữ hoa chữ thường) trong bảng products.


print(result) # in ra tất cả các sản phẩm có tên là 'Laptop' hoặc 'Smartphone' từ bảng products.
print(query) # in ra tất cả các sản phẩm có tên là None từ bảng products.
print(like_query) # in ra tất cả các sản phẩm có tên chứa 'Laptop' từ bảng products.
print(ilike_query) # in ra tất cả các sản phẩm có tên chứa 'laptop' (không phân biệt chữ hoa chữ thường) từ bảng products.

session.close()