# OOP - Class Variable, __dict__ và Cách Python Xử Lý Biến Instance, Class
Class variable (biến lớp) là một biến được định nghĩa bên ngoài các phương thức của lớp, nhưng bên trong lớp đó. Những biến này không thuộc về một đối tượng cụ thể (instance), mà thuộc về toàn bộ lớp, nghĩa là tất cả các đối tượng được tạo ra từ lớp đó sẽ chia sẻ giá trị của biến lớp.
- Đặc điểm của class variable:
+ Chia sẻ giá trị giữa các đối tượng: Nếu một đối tượng thay đổi giá trị của class variable, tất cả các đối tượng khác của lớp đó cũng sẽ thấy sự thay đổi, vì class variable là một phần của lớp, không phải của mỗi đối tượng riêng biệt.
+ Có thể truy cập qua lớp hoặc đối tượng: Bạn có thể truy cập class variable thông qua tên lớp hoặc thông qua đối tượng, nhưng nó sẽ luôn là thuộc tính chung cho tất cả các đối tượng của lớp.
class Employee:

    salary_up = 2

    def __init__(self, first_name, last_name, age, address, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.salary = salary
    def get_fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def increase_salary(self):
        self.salary = self.salary * self.salary_up


emp_1 = Employee('Nguyen', 'Tam', 19, 'Ha Noi', 1000)
emp_2 = Employee('Duong', 'Dat', 25, 'Ha Noi', 1000)

emp_1.increase_salary()
emp_2.increase_salary()

print(emp_1.salary)
print(emp_2.salary)
# Phương thức __dict__ là một thuộc tính đặc biệt của đối tượng và lớp trong Python. Nó trả về một từ điển (dictionary)
chứa tất cả các thuộc tính và phương thức của đối tượng hoặc lớp đó.

# + Đối với object instance (đối tượng), __dict__ sẽ chứa tất cả các thuộc tính của đối tượng đó.
# + Đối với class (lớp), __dict__ sẽ chứa tất cả các class variables và phương thức (method) của lớp.

emp_1.__dict__
# Khi gọi đến một class variable thì python nó sẽ xử lý ???

emp_1.salary_up  // đầu tiên python sẽ xem salary_up atribute => nó sẽ bắt đầu tìm đến salary_up ở class variable

Employee.salary_up = 4

emp_1.increase_salary()
emp_2.increase_salary()

print(Employee.salary_up)
print(emp_1.salary_up)
print(emp_2.salary_up)