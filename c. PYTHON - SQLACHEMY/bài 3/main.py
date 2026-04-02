from models import engine, Product
from sqlalchemy.orm import Session

session = Session(bind=engine)

# order_by là một phương thức được sử dụng để sắp xếp kết quả truy vấn theo một hoặc nhiều cột
# Mặc định asc sắp xếp tăng dần và desc sắp xếp giảm dần

product_list = ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard']
price_list = [1500.0, 800.0, 500.0, 300.0, 100.0]

for _ in range(5): # Duyệt qua một phạm vi từ 0 đến 4 (tổng cộng 5 lần) để tạo và thêm các sản phẩm mới vào session.
    new_product = Product(name=product_list[_], price=price_list[_]) 
    session.add(new_product)

session.commit()
session.close() # đóng session khi hoàn thành 