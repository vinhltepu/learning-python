from models import engine , Product
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_ , not_


Session = Session(bind=engine)

if not Session.query(Product).first():
    Session.add_all([
        Product(name='Laptop', price=1500.0),
        Product(name='Smartphone', price=1200.0),
        Product(name='Tablet', price=900.0),
        Product(name='Headphones', price=250.0),
        Product(name='Smartphone', price=1100.0)
    ])
    Session.commit()

# filter_by() được sử dụng để lọc các sản phẩm có giá lớn hơn 1000.0. 
product = Session.query(Product).filter(Product.price > 1000.0).all() # Truy vấn tất cả các sản phẩm có giá lớn hơn 1000.0 từ bảng products

product = Session.query(Product).filter(Product.name == 'Laptop').first() # Truy vấn sản phẩm đầu tiên có tên là 'Laptop' từ bảng products

product = Session.query(Product).filter(or_(Product.price > 1000.0, Product.name == 'Smartphone')).all() # Truy vấn tất cả các sản phẩm có giá lớn hơn 1000.0 hoặc có tên là 'Smartphone' từ bảng products

product = Session.query(Product).filter(Product.name.like('%phone%')).all() # Truy vấn tất cả các sản phẩm có tên chứa chuỗi 'phone' từ bảng products. Phương thức like() được sử dụng để thực hiện tìm kiếm theo mẫu, và '%phone%' có nghĩa là tìm kiếm bất kỳ chuỗi nào chứa 'phone'.

product = Session.query(Product).filter(Product.name.ilike('%phone%')).all() # Truy vấn tất cả các sản phẩm có tên chứa chuỗi 'phone' không phân biệt chữ hoa chữ thường từ bảng products. Phương thức ilike() tương tự như like() nhưng không phân biệt chữ hoa chữ thường.
# and_() được sử dụng để kết hợp nhiều điều kiện với nhau
product = Session.query(Product).where(and_(Product.price > 1000.0, Product.name.like('%phone%'))).all() # Truy vấn tất cả các sản phẩm có giá lớn hơn 1000.0 và có tên chứa chuỗi 'phone' từ bảng products. Phương thức where() được sử dụng để áp dụng điều kiện lọc, và and_() được sử dụng để kết hợp nhiều điều kiện với nhau.
# not_() được sử dụng để phủ định một điều kiện
product = Session.query(Product).where(not_(Product.price > 1000.0)).all() # Truy vấn tất cả các sản phẩm có giá không lớn hơn 1000.0 từ bảng products. Phương thức not_() được sử dụng để phủ định điều kiện, có nghĩa là chúng ta đang tìm kiếm các sản phẩm có giá nhỏ hơn hoặc bằng 1000.0.

print(product) 

Session.close()