from models import engine , Product
from sqlalchemy.orm import Session

# Engine dùng để kết nối tới cơ sở dữ liệu
# Base dùng để tạo cơ sở dữ liệu và bảng.
# Session dùng để quản lý và thao tác dữ liệu trong các bảng đó. 

session = Session(bind=engine)
# Đây là phầm thêm dữ liệu cho bảng products
new_product_1 = Product(name="Laptop", price=1500.0) # Tạo một sản phẩm mới với tên "Laptop" và giá 1500.0
new_product_2 = Product(name="Smartphone", price=800.0) # Tạo một sản phẩm mới với tên "Smartphone" và giá 800.0
session.add_all([new_product_1, new_product_2])            # Thêm các sản phẩm mới vào session. Phương thức add_all() được sử dụng để thêm nhiều đối tượng cùng một lúc vào session. Ở đây, chúng ta thêm cả new_product_1 và new_product_2 vào session để chuẩn bị cho việc lưu chúng vào cơ sở dữ liệu. 
session.commit()# Lưu các thay đổi vào cơ sở dữ liệu. Khi gọi commit(), tất cả các thay đổi đã được thực hiện trong session sẽ được ghi vào cơ sở dữ liệu, bao gồm việc thêm sản phẩm mới mà chúng ta vừa tạo.

#đây là phần lấy dữ liệu ra từ bảng products - read 
products = session.query(Product).all() # Truy vấn tất cả các sản phẩm từ bảng products. Phương thức query() được sử dụng để tạo một truy vấn mới, và all() được gọi để lấy tất cả các kết quả của truy vấn đó. Kết quả sẽ là một danh sách các đối tượng Product đại diện cho tất cả các sản phẩm trong bảng products.
for product in products: # Duyệt qua từng sản phẩm trong danh sách products và in ra tên và giá của mỗi sản phẩm. 
    print(f"Product Name: {product.name}, Price: {product.price}") # In ra tên và giá của mỗi sản phẩm. 


# update dữ liệu 
products[0].price = 1400.0 # Cập nhật giá của sản phẩm đầu tiên trong danh sách 
products[1].name = "Smartphone Pro" # Cập nhật tên của sản phẩm thứ hai trong danh sách
session.commit() 


# delete dữ liệu
session.delete(products[0]) # Xóa sản phẩm đầu tiên trong danh sách products khỏi session
session.delete(products[1]) # Xóa sản phẩm thứ hai trong danh sách products khỏi session
session.commit() 