# tìm hiểu  Class, Object __init__ và self
OOP (Object-Oriented Programming - Lập trình hướng đối tượng) là một phương pháp lập trình tổ chức và thiết kế phần mềm dựa trên các đối tượng (objects). Các đối tượng này là sự kết hợp của dữ liệu (thuộc tính) và các phương thức (hàm) thao tác trên dữ liệu đó. OOP giúp mã nguồn dễ duy trì, mở rộng và tái sử dụng.
# Ví dụ: Một công ty có Rất nhiều nhân viên (Employee)
- Employee:
 + first_name
 + last_name
 + age
 + address
 + salary
# Class (Lớp):
Lớp là một khuôn mẫu (template) để tạo ra các đối tượng (objects). Nó định nghĩa các thuộc tính (properties|
attributes) và phương thức (methods - function) mà các đối tượng của lớp đó sẽ có.
Một lớp có thể chứa các biến và hàm, trong đó các biến được gọi là attributes (thuộc tính) và các hàm được gọi l
methods (phương thức).

# vd 
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

emp_1.first_name = 'Nguyen'
emp_1.last_name = 'Tam'
emp_1.age = 19
emp_1.address = 'Ha Noi'
emp_1.salary = 1000

emp_2.first_name = 'Duong'
emp_2.last_name = 'Dat'
emp_2.age = 19
emp_2.address = 'Ha Noi'
emp_2.salary = 1000

print(emp_1,last_name)
print(emp_2,last_name)

# Instance (Object):
Instance (hoặc Object) là một thực thể cụ thể được tạo ra từ lớp. Khi bạn tạo một instance của một lớp, bạn đã tạo ra một đối tượng của lớp đó.
Mỗi đối tượng có thể có các giá trị thuộc tính khác nhau, nhưng chúng sẽ sử dụng các phương thức giống nhau (từ lớp).
# Phương thức 
__init__ trong Python là một phương thức đặc biệt, còn gọi là constructor (hàm khởi tạo), được gọi tự động
mỗi khi bạn tạo một đối tượng từ một lớp. Nó cho phép bạn thiết lập các giá trị ban đầu cho các thuộc tính của đối tượng
khi đối tượng được khởi tạo.
# self là tham chiếu đến chính đối tượng (instance) của lớp mà bạn đang làm việc.
Nó giúp bạn truy cập các thuộc tính và phương thức của đối tượng trong lớp.
self không phải là từ khóa bắt buộc trong Python, nhưng đây là một quy ước phổ biến mà mọi lập trình viên Python đều tuân theo. Bạn có thể dùng tên khác, nhưng self là chuẩn và dễ đọc.
# vd
class Employee:
    def __init__(self, first_name, last_name, age, address, salary): // self sẽ nhận biến số đầu tiên như là emp1 và emp2
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.salary = salary
# phương thức method là một hàm liên quan tới 1 lớp 
    def get full_time(self) -> str :
        return f"{self.firt_name}+{full_name}"

emp_1 = Employee('Nguyen', 'Tam', 19, 'Ha Noi', 1000)
emp_2 = Employee('Duong', 'Dat', 25, 'Ha Noi', 2000)

print(emp_1,full_name)
print(emp_2,full_name)
