from models import User, engine, Post
from sqlalchemy.orm import Session
from sqlalchemy import text

session = Session(bind=engine)
sql = text("SELECT * FROM users") # Truy vấn tất cả các bản ghi từ bảng users
result = session.execute(sql) # Duyệt qua kết quả và in ra từng bản ghi
for row in result:# Duyệt qua kết quả và in ra từng bản ghi
    print(row)
session.execute( text("DELETE FROM posts") ) # Xóa tất cả các bản ghi trong bảng posts
session.execute( text("DELETE FROM users") )# Xóa tất cả các bản ghi trong bảng users
session.commit()
# create user 
user = session.query(User).filter_by(name="Hanki").first() # Truy vấn người dùng có tên là 'Hanki' từ bảng users
if not user:
    user = User(name="Hanki", age=30) # Tạo một đối tượng User mới với tên 'Hanki' và tuổi 30
    session.add(user) # Thêm đối tượng User vào phiên làm việc của SQLAlchemy

# create post
post = Post(title="mặt hàng ", content="điện thoại ", User_id=1)
session.add(post)

session.commit()
session.close()