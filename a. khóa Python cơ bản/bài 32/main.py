#Bài 1: Quản lý họ tên nhân viên với @property
#Yêu cầu
#Tạo class Employee
#Có first_name, last_name
#ạo @property tên fullname
#Tạo setter cho fullname
#Tạo deleter cho fullname

class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @fullname.setter
    def fullname(self, new_fullname):
        first_name, last_name = new_fullname.split(" ")
        self.first_name = first_name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        self.first_name = ""
        self.last_name = ""
        print("Da xoa fullname")


emp = Employee("Tran", "Van A")

print(emp.fullname)

emp.fullname = "Tran Van B"
print(emp.fullname)

del emp.fullname
print(emp.fullname)

#Bài 2: Quản lý email với getter, setter, deleter
#Yêu cầu
#Tạo class Employee
#Tạo thuộc tính _email
#Tạo getter cho email
#Tạo setter để đổi email
#Tạo deleter để xóa email

class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._email = f"{first_name}.{last_name}@gmail.com"

    @property
    def email(self):
        return f"Email cua nhan vien la: {self._email}"

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @email.deleter
    def email(self):
        self._email = "Da xoa email"

        
emp = Employee("Nguyen", "T")

print(emp.email)

emp.email = "abc@gmail.com"
print(emp.email)

del emp.email
print(emp.email)

#Bài 3: Quản lý điểm học sinh
#Yêu cầu
#Tạo class Student
#Tạo thuộc tính _score
#Tạo getter cho score
#Tạo setter kiểm tra điểm từ 0 đến 10
#Tạo deleter để xóa điểm

class Student:

    def __init__(self, name, score):
        self.name = name
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if 0 <= new_score <= 10:
            self._score = new_score
        else:
            print("Diem khong hop le")

    @score.deleter
    def score(self):
        self._score = 0
        print("Da xoa diem, gan ve 0")


st = Student("A", 8)

print(st.score)

st.score = 9
print(st.score)

st.score = 15
print(st.score)

del st.score
print(st.score)
