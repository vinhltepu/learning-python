#1) Bài tập 1: Tạo lớp Student
##Đề bài
#Tạo lớp Student có:
#Thuộc tính: name, age, grade
#Hàm khởi tạo __init__
#Method show_info() để in thông tin học sinh

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):
        print("Tên:", self.name)
        print("Tuổi:", self.age)
        print("Lớp:", self.grade)


st1 = Student("A", 21, "Kỹ thuật phần mềm")
st1.show_info()

#2) Bài tập 2: Tạo 2 object từ cùng một class
#Đề bài
#Tạo lớp Employee có:
#Thuộc tính: first_name, last_name, salary
#Tạo 2 nhân viên khác nhau
#In ra thông tin của từng người bằng method full_name() và show_salary()

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def full_name(self):
        return self.first_name + " " + self.last_name

    def show_salary(self):
        print("Lương:", self.salary)


emp1 = Employee("NGUYEM", "A", 1000)
emp2 = Employee("TRAN", "B", 2000)

print(emp1.full_name())
emp1.show_salary()

print(emp2.full_name())
emp2.show_salary()

#3) Bài tập 3: Tính diện tích hình chữ nhật
#Đề bài
#Tạo lớp Rectangle có:
#Thuộc tính width, height
#Method area() để tính diện tích
#Method show_info() để in chiều dài, chiều rộng, diện tích

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def show_info(self):
        print("Chiều rộng:", self.width)
        print("Chiều cao:", self.height)
        print("Diện tích:", self.area())


hcn = Rectangle(5, 10)
hcn.show_info()