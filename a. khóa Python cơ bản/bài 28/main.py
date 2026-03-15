#Bài 1: Quản lý học sinh với class variable
#Yêu cầu
#ạo class Student
#Tạo class variable tên là school_name = 'ABC School'
#Tạo 2 object học sinh với các thuộc tính: name, age, score
#In ra tên trường bằng cách gọi từ class và từ object

class Student:
    school_name = 'ABC School'

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

student1 = Student("A", 20, 85)
student2 = Student("B", 22, 90)

print(Student.school_name)

print(student1.school_name)
print(student2.school_name)

#Bài 2: Tăng giá sản phẩm và xem __dict__
#Yêu cầu
#Tạo class Product
#Tạo class variable tên là price_up = 2
#Tạo method increase_price() để tăng giá
#In __dict__ của một object để xem các thuộc tính bên trong

class Product:

    price_up = 2

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_info(self) -> str:
        return f"{self.name} - {self.price} - {self.quantity}"

    def increase_price(self):
        self.price = self.price * self.price_up


pd_1 = Product('A', 5000, 10)
pd_2 = Product('B', 10000, 5)

pd_1.increase_price()
pd_2.increase_price()

print(pd_1.price)
print(pd_2.price)

print(pd_1.__dict__)

#Bài 3: Python ưu tiên tìm biến ở đâu
#Yêu cầu
#Tạo class Employee có class variable là salary_up = 2
#Tạo 2 object nhân viên
#Đổi Employee.salary_up = 3
#In ra Employee.salary_up, emp_1.salary_up, emp_2.salary_up

class Employee:

    salary_up = 2

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def increase_salary(self):
        self.salary = self.salary * self.salary_up


emp_1 = Employee('A', 'B', 1000)
emp_2 = Employee('C', 'D', 2000)

Employee.salary_up = 3

emp_1.increase_salary()
emp_2.increase_salary()

print(Employee.salary_up)
print(emp_1.salary_up)
print(emp_2.salary_up)

print(emp_1.salary)
print(emp_2.salary)