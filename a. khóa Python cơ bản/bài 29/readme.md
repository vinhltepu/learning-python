#  Class Method và Static Method trong Python
method thông thường => nhận đối tượng (object | instance) làm đối số đầu tiên
class method
static method

# classmethod:
Phương thức này nhận tham số đầu tiên là cls, thay vì self như các phương thức thông thường.
cls đại diện cho class, không phải là instance. Do đó, bạn có thể gọi phương thức này từ chính class hoặc từ instance của class.
Thường được sử dụng khi bạn cần truy cập hoặc thay đổi thuộc tính của class, tạo ra đối tượng.

class Employee:

    salary_up = 2  // class variable, dùng chung cho tất cả object
    nums_of_object = 0  // class variable, đếm số object đã tạo

    def __init__(self, first_name, last_name, age, address, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.salary = salary

        Employee.nums_of_object += 1   # NOTE: mỗi lần tạo object mới thì tăng biến đếm lên 1

    def get_fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"  

    def increase_salary(self):
        self.salary = self.salary * self.salary_up // self.salary_up sẽ tìm ở object trước, không có thì lấy ở class

    @classmethod
    def changed_salary_up(cls, value):
        cls.salary_up = value    # NOTE: cls đại diện cho class, dùng để đổi class variable

    @classmethod
    def create_emp(cls):
        return cls('A', 'NGUYEN', 20, 'TPHCM', 3000)  // tạo object từ classmethod


emp_1 = Employee('Nguyen', 'Tam', 19, 'Ha Noi', 1000)
emp_2 = Employee('Duong', 'Dat', 25, 'Ha Noi', 1000)

emp_3 = Employee.create_emp()  // gọi classmethod bằng tên class để tạo object mới

print(emp_3.salary)

# staticmethod:
phương thức này không nhận tham số đặc biệt nào (không phải self hay cls).
dây chỉ là một phương thức bình thường, nhưng bạn vẫn có thể gọi nó qua class mà không cần tạo instance. Nó không thuộc vào dữ liệu của class hoặc instance.
thường được sử dụng khi phương thức không cần truy cập vào bất kỳ thông tin nào của class hoặc instance.


class Employee:

    salary_up = 2  // class variable, dùng chung cho tất cả object
    nums_of_object = 0  // class variable, đếm số object đã tạo

    def __init__(self, first_name, last_name, age, address, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.salary = salary

        Employee.nums_of_object += 1   # NOTE: mỗi lần tạo object mới thì tăng biến đếm lên 1

    def get_fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"  

    def increase_salary(self):
        self.salary = self.salary * self.salary_up // self.salary_up sẽ tìm ở object trước, không có thì lấy ở class

    @classmethod
    def changed_salary_up(cls, value):
        cls.salary_up = value    # NOTE: cls đại diện cho class, dùng để đổi class variable

    @classmethod
    def create_emp(cls):
        return cls('A', 'NGUYEN', 20, 'TPHCM', 3000)  // tạo object từ classmethod
    

    @staticmethod // tạo staticmehod
    def sum ():
        print (5+10)
        


emp_1 = Employee('Nguyen', 'Tam', 19, 'Ha Noi', 1000)
emp_2 = Employee('Duong', 'Dat', 25, 'Ha Noi', 1000)

Employee.sum()