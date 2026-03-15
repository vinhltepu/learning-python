# Kế thừa (Inheritance) và Các Khái Niệm Quan Trọng
Kế thừa (inheritance) là một trong những đặc điểm nổi bật của lập trình hướng đối tượng (OOP). Nó cho phép một lớp (class) mới kế thừa các thuộc tính (attributes) và phương thức (methods) từ một lớp khác. Điều này giúp tái sử dụng code, giảm sự trùng lặp và dễ bảo trì hơn.

# vd 
class Employee: // lớp cha dùng để mô tả thông tin như tên tuổi ... 

    salary_up = 2 // đây là biến lớp , tất cả object tạo từ class Employee hoặc class con kế thừa từ nó đều có thể dùng giá trị này ,ở đây đang quy định hệ số tăng lương là 2

    def __init__(self, first_name, last_name, age, address, salary): // hàm khởi động object 
        self.last_name = last_name
        self.age = age
        self.address = address
        self.salary = salary

    def get_fullname(self) -> str: // hàm này trả về họ và tên đầy đủ
        return f"{self.first_name} {self.last_name}"

    def increase_salary(self): //hàm này tăng lương theo hệ số salary_up
        self.salary = self.salary * self.salary_up


class Saler(Employee): // Saler là lớp con , Employee là lớp cha và Saler sẽ kế thừa toàn bộ thuộc tính và phương thức của Employee
    pass


emp_1 = Saler('Nguyen', 'Tam', 19, 'Ha Noi', 1000)
emp_2 = Saler('Duong', 'Dat', 25, 'Ha Noi', 1000)

print(help(Saler))





# output
class Saler(Employee)
Saler(first_name, last_name, age, address, salary)

Method resolution order:
    Saler
    Employee
    builtins.object

Methods inherited from Employee:

__init__(self, first_name, last_name, age, address, salary)

__dict__
    dictionary for instance variables

__weakref__
    list of weak references to the object

----------------------------------------------------------------

Data and other attributes inherited from Employee:

salary_up = 2

None



# ghi đè thuộc tính 
# ghi đè phương thức 
class Employee:
    salary_up = 2   // Thuộc tính của lớp cha

    def __init__(self, first_name, last_name, age, address, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.salary = salary

    def get_fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def increase_salary(self):
        self.salary = self.salary * self.salary_up   // Dùng salary_up hiện tại của object/class


class Saler(Employee): // override thuộc tính:
    salary_up = 0   // Ghi đè 
                    //Employee.salary_up = 2
                    // nhưng ở class con Saler thì salary_up bị override thành 0 

    pass            //Chưa ghi đè phương thức nào


emp_1 = Saler('Nguyen', 'Tam', 19, 'Ha Noi', 1000)
emp_2 = Saler('Duong', 'Dat', 25, 'Ha Noi', 1000)

print('--------Lương trước khi tăng')
print(emp_1.salary)
print(emp_2.salary)

emp_1.increase_salary()
emp_2.increase_salary()

print('--------Lương sau khi tăng')
print(emp_1.salary)
print(emp_2.salary)

# super 
class Employee:
    salary_up = 2   // Thuộc tính lớp của class cha

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


class Saler(Employee):   // Kế thừa từ Employee
    def __init__(self, first_name, last_name, age, address, salary, product):
        super().__init__(first_name, last_name, age, address, salary)  
        // super() gọi __init__ của class cha Employee
         //để gán lại các thuộc tính chung:
         //self.first_name, self.last_name, self.age, self.address, self.salary

        self.product = product  
        // Thuộc tính riêng thêm vào cho class Saler
        // super() có tác dụng là gọi lại phương thức __init__ của lớp cha Employee để tận dụng phần code khởi tạo có sẵn

emp_1 = Saler('Nguyen', 'Tam', 19, 'Ha Noi', 1000, 'Quần Jean')
emp_2 = Saler('Duong', 'Dat', 25, 'Ha Noi', 1000, 'Áo ba lỗ')

print(emp_1.product)
print(emp_2.product)

# hàm isinstance , issubclass
class Employee:
    salary_up = 2   // Thuộc tính lớp của class cha

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


class Saler(Employee):
    def __init__(self, first_name, last_name, age, address, salary, product):
        super().__init__(first_name, last_name, age, address, salary)
        self.product = product


class Manager(Employee):
    def __init__(self, first_name, last_name, age, address, salary):
        super().__init__(first_name, last_name, age, address, salary)

            self.list_emps: list = []

    def add_emp(self, emp: Saler):
        self.list_emps.append(emp)

    def print_emps(self):
        if self.list_emps:
            for emp in self.list_emps:
                print('full_name of saler:', emp.get_fullname())
        elsse: 
            print('không có nhân viên nào cả')

manager = Manager('Thanh', 'Tran', 20, 'TPHCM', 3000)

emp_1 = Saler('Nguyen', 'Tam', 19, 'Ha Noi', 1000, 'Quần Jean')
emp_2 = Saler('Duong', 'Dat', 25, 'Ha Noi', 1000, 'Áo ba lỗ')

print(isinstance(manager, Saler)) // object manager có phải là một thể hiện (instance) của class Saler hay không 

print(issubclass(Manager, Employee)) // class Manager có phải là lớp con của Employee hay không 

# đa kế thừa 
class A:
    def method_A(self):
        print('Đây là method A')


class B:
    def method_A(self):
        print('Đây là method B')


class C(B, A): // C kế thừa từ 2 lớp là B và A 
    pass


c = C()

c.method_A() // Python sẽ tìm method theo MRO 

# method resolution order
print(C.mro()) // Dòng này dùng để xem thứ tự tìm kiếm



# Kế thừa đa cấp 
class A:
    def method_A():
        print('A')


class B(A): // kế thừa nhiều tầng B kế thừa từ A 
    def method_B():
        print('B')


class C(B):  // kế thừa nhiều tầng  C kế thừa từ B và C sẽ dùng được cả method của B và method của A
    pass


c = C() // C không viết method nào nhưng vẫn dùng được vì method_A() được kế thừa từ A , method_B() được kế thừa từ B

c.method_A()
c.method_B()





