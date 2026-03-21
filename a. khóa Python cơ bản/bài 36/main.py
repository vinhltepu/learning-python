# Hướng dẫn sử dụng SQLite3 trong Python - Tạo cơ sở dữ liệu, thao tác CRUD và bảo mật SQL 
#SQLite là một cơ sở dữ liệu nhúng, có nghĩa là nó không cần một server riêng biệt để vận hành và có thể tích hợp trực tiếp vào 
#ứng dụng (ví dụ như ứng dụng di động, ứng dụng máy tính để bàn) mà không cần cài đặt phần mềm máy chủ riêng biệt. 

# SQlite nó thuộc cơ sở dữ liệu quan hệ , có nghĩa là nó lưu trữ dữ liệu trong các bảng có cấu trúc , và hỗ trợ các mối quan hệ giữa các bảng thông qua khóa chính và khóa ngoại'
import sqlite3

conn = sqlite3.connect('mydatabase') # Tên file

# Đặt tên cho file cơ sở dữ liệu của mình với bất kỳ phần mở rộng nào, nhưng thông thường người ta sẽ sử dụng phần mở rộng .db hoặc .sqlite hoặc .sqlite3. 
# Đây chỉ là các quy ước chung để dễ dàng nhận diện các file cơ sở dữ liệu SQLitept

# Cần phải tạo bảng users

c = conn.cursor() # để thực thi các câu lệnh sqlite

# Viết câu lệnh để tạo bảng users
# + username: Varchar
# + password: Varchar
# + address: Varchar
# + age: Float


# NULL. Giá trị là giá trị rỗng (NULL).
# INTEGER. Giá trị là một số nguyên có dấu, được lưu trữ trong 0, 1, 2, 3, 4, 6 hoặc 8 byte tùy theo độ lớn của giá trị.
# REAL. Giá trị là một số thực dấu phẩy động, được lưu trữ dưới dạng số dấu phẩy động IEEE 8 byte.
# TEXT. Giá trị là một chuỗi văn bản, được lưu trữ bằng bộ mã hóa của cơ sở dữ liệu (UTF-8, UTF-16BE hoặc UTF-16LE).
# BLOB. Giá trị là một khối dữ liệu nhị phân, được lưu trữ đúng như dữ liệu đầu vào.
# NULL. The value is a NULL value.

sql: str = """
CREATE TABLE users(
   username TEXT,
   password TEXT,
   address TEXT,
   age REAL
)
"""





# c.execute("""
# INSERT INTO users VALUES (1, 'thanh', 'tam123', 'Ha Noi', 19);
# """)

# c.execute("""
# INSERT INTO users VALUES (2, 'vinh', 'databc', 'Ha Noi', 21);
# """)

# Tại sao dữ liệu vẫn chưa vào file mydatabase.db.
# Khi mà bạn có bất kì thay đổi dữ liệu nào như là việc (Nhập dữ liệu, Cập nhật dữ liệu, Xóa dữ liệu)
# Tuy nó chưa hề được xác nhận vào cơ sở dữ liệu





# update dữ liệu 

# c.execute("""
# UPDATE users
# SET password = 'dat123'
# WHERE id = 2;
# """)



# Delete dữ liệu

# c.execute("""
# DELETE FROM users
# WHERE id = 2;
# """)

# READ (Lấy dữ liệu lên)
#c.execute("""
#SELECT * From users;
#""")
#users = c.fetchall()
#for user in users:
#    print(user)

#SELECT là lấy dữ liệu
#* là lấy tất cả cột
#FROM users là lấy từ bảng users


# - 2 cách:
# + Sử dụng dấu ? và tham số thứ 2 là tuple
# + Sử dụng :name và sử dụng tham số thứ 2 là dict

# c.execute("""
# INSERT INTO users VALUES (?, ?, ?, ?, ?)
# """, (2, 'nhi', 'nhi321', 'Ha Noi', 19))

#c.execute("""
#INSERT INTO users VALUES (:id, :username, :password, :address, :age)
#""",
#{
#    "id": 3,
#    "username": 'Vinh',
#    "password": "12345@",
#    "address": 'HNOI',
#    "age": 22 
#})



# c.execute('SELECT * FROM users WHERE id = ?', (1,))

# Tạo ra function => CRUD => CREATE READ UPDATE DELETE

#class User:
#    def __init__(self, id, username, password, address, age):
#        self.id = id
#        self.username = username
#        self.password = password
#        self.address = address
#        self.age = age
#
#    def __repr__(self):
#        return f"User({self.id}, {self.username}, {self.password}, {self.address}, {self.age})"



c.execute('SELECT * FROM users WHERE id = :id', {"id": 1})

def create_user(user: User):
    c.execute("""
        INSERT INTO users VALUES (?, ?, ?, ?, ?);
    """, (user.id, user.username, user.password, user.address, user.age))
    conn.commit()

def read_user(user_name: str):
    c.execute("""
        SELECT * FROM users WHERE username = ?;
    """, (user_name,))
    return c.fetchall() # trả về tất cả các dòng dữ liệu th

def update_user_name(user: User):
    c.execute("""
        UPDATE users
        SET username = :name
        WHERE id = :id 
    """, {"name": user.username, "id": user.id})
    conn.commit()


def delete_user_by_id(user: User):
    c.execute("""
        DELETE FROM users
        WHERE id = :id
    """, {"id": user.id})
    conn.commit()

# CREATE user
#u1 = User(4, 'Thai', 'Thai123', 'Viet Nam', 20)
#u2 = User(5, 'Viet', 'VietGa', 'Trung Quoc', 24)
#create_user(u1)
#create_user(u2)


# READ user
# u3 = User(4, 'tam', 'Thai123', 'Viet Nam', 20)
# users = read_user_by_name(u3)
# print(users)


# UPDATE user
# u4 = User(1, 'tam', 'Thai123', 'Viet Nam', 20)
# update_user_name(u4)

# DELETE user

#u4 = User(5, 'tam', 'Thai123', 'Viet Nam', 20)
#delete_user_by_id(u4)

conn.commit() # xác nhận các thay đổi vào cơ sở dữ liệu 

conn.close () # đóng kết nối với cơ sở dữ liệu 