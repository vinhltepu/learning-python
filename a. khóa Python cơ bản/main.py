#Bài 1: Quản lý nhân viên
#Yêu cầu
#Tạo class Employee
#Có class variable là salary_up = 2
#Tạo classmethod để đổi salary_up

class Employee:
    salary_up = 2
    nums_of_object = 0

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

        Employee.nums_of_object += 1

    def get_fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def increase_salary(self):
        self.salary = self.salary * self.salary_up

    @classmethod
    def change_salary_up(cls, value):
        cls.salary_up = value

    @staticmethod
    def sum_number(a, b):
        return a + b


emp_1 = Employee('Nguyen', 'A', 1000)
emp_2 = Employee('Duong', 'B', 2000)

print(emp_1.get_fullname())
print(emp_2.get_fullname())

Employee.change_salary_up(3)

emp_1.increase_salary()
emp_2.increase_salary()

print(emp_1.salary)
print(emp_2.salary)

print(Employee.sum_number(5, 10))

#Bài 2: Quản lý học sinh
#Yêu cầu
#Tạo class Student
#Có class variable là school_name = 'ABC School'
#Tạo classmethod để đổi tên trường
#Tạo staticmethod để kiểm tra điểm đậu hay rớt

class Student:
    school_name = 'ABC School'

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_info(self) -> str:
        return f"{self.name} - {self.age} - {self.score}"

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def is_pass(score):
        return score >= 5


st_1 = Student('ban A', 18, 8)
st_2 = Student('Ban B', 17, 4)

print(st_1.get_info())
print(st_2.get_info())

print(Student.school_name)

Student.change_school_name('XYZ School')

print(Student.school_name)
print(st_1.school_name)
print(st_2.school_name)

print(Student.is_pass(st_1.score))
print(Student.is_pass(st_2.score))

#Bài 3: Quản lý sản phẩm
#Yêu cầu
#Tạo class Product
#Có class variable là tax = 0.1
#Tạo classmethod để đổi thuế
#Tạo staticmethod để tính tiền sau thuế

class Product:
    tax = 0.1

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self) -> str:
        return f"{self.name} - {self.price}"

    @classmethod
    def change_tax(cls, new_tax):
        cls.tax = new_tax

    @staticmethod
    def final_price(price, tax):
        return price + price * tax


pd_1 = Product('A', 10000)
pd_2 = Product('B', 20000)

print(pd_1.get_info())
print(pd_2.get_info())

print(Product.tax)

Product.change_tax(0.2)

print(Product.tax)
print(pd_1.tax)
print(pd_2.tax)

print(Product.final_price(pd_1.price, Product.tax))
print(Product.final_price(pd_2.price, Product.tax))