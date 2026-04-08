Nếu mà  lưu trữ hết dữ liệu vào trong 1 bảng => nó cũng đc nhé => Nhưng nó chưa được tối ưu
Mối quan hệ: 1 - nhiều

# users
1 user thì có nhiều bài posts

# posts
nhiều bài posts thì thuộc 1 user

# - users:
+ id INT PRIMARY KEY
+ name STRING

# - posts:
+ id INT PRIMARY KEY
+ title STRING
+ desciption STRING
+ user_id INT FOREIGN KEY users.id

