from models import engine, Product
from sqlalchemy.orm import Session
from sqlalchemy import  func

# Trong SQLAlchemy, các câu lệnh truy vấn (như session.query(...).filter(...)) không thực sự thực thi 
# cho đến khi bạn gọi phương thức như .all(), .first(), .one(), hoặc bất kỳ phương thức nào lấy kết quả. 
# Điều này được gọi là lazy loading (tải lười).

# group by là một phương thức được sử dụng để nhóm các kết quả truy vấn theo một hoặc nhiều cột.


session = Session(bind=engine)

if not session.query(Product).first():
    session.add_all([
        Product(name='Laptop', price=1500.0),
        Product(name='Smartphone', price=1200.0),
        Product(name='Tablet', price=900.0),
        Product(name='Laptop', price=1700.0),
    ])
    session.commit()

# Group by và count
count_list = session.query(func.count(Product.id)).filter(Product.price > 1000.0).group_by(Product.name).all()
products = session.query(Product).filter(Product.price > 1000.0).group_by(Product.name).all()

print('Số lượng sản phẩm giá > 1000 theo tên:', count_list)
for p in products:
    print(f"{p.id}: {p.name} - {p.price}")

session.close()