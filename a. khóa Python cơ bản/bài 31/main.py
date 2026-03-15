#Bài 1: __init__, __str__, __repr__
#Yêu cầu
#Tạo thêm object s2 với thông tin tự chọn.
#In s2 bằng print(s2). # type: ignore
#In biểu diễn chính thức của s2 bằng repr(s2).
#Đổi điểm của s1 thành 9.0 rồi in lại object

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f'Sinh viên: {self.name}, tuổi: {self.age}, điểm: {self.score}'

    def __repr__(self):
        return f'Student({self.name}, {self.age}, {self.score})'


s1 = Student('An', 20, 8.5)
print(s1)
print(repr(s1))

#Bài 2: __del__
#Yêu cầu
#Tạo thêm object e2 với tên bất kỳ.
#Dùng del e1 để xóa object e1.
#Dùng del e2 để xóa object e2.
#Quan sát kết quả in ra và ghi chú: __del__ có thể không phải lúc nào cũng chạy đúng thời điểm bạn mong muốn.

class Employee:
    def __init__(self, fullname):
        self.fullname = fullname

    def __del__(self):
        print(self.fullname, "đã bị hủy")


e1 = Employee("Nguyễn Văn A")

#Bài 3: __eq__, __ne__
#Yêu cầu
#Kiểm tra p1 == p2.
#Kiểm tra p1 != p3.
#Tạo thêm p4 = Product("Tẩy", 7000) rồi kiểm tra p3 == p4.
#Đổi giá của p2 thành 9000 rồi kiểm tra lại p1 == p2.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price


p1 = Product("Bút", 5000)
p2 = Product("Vở", 5000)
p3 = Product("Sách", 7000)

#Bài 4: __lt__, __gt__, __le__, __ge__
#Yêu cầu
#Kiểm tra b1 < b2.
#Kiểm tra b2 > b1.
#Kiểm tra b1 <= b3.
#Kiểm tra b2 >= b3.

class Box:
    def __init__(self, weight):
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight


b1 = Box(10)
b2 = Box(15)
b3 = Box(10)

#Bài 5: __add__, __sub__
#Yêu cầu
#Tính m1 + m2 và in kết quả.
#Tính m1 - m2 và in kết quả.
#Tạo thêm m3 = Money(2000) rồi tính m1 + m2 + m3.
#Thử tính m2 - m1 và xem kết quả.

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __str__(self):
        return f'{self.amount} VND'


m1 = Money(10000)
m2 = Money(3000)
m3 = Money(2000)

#Bài 6: __mul__, __truediv__, __floordiv__, __mod__
#Yêu cầu
#Tính n1 * n2.
#Tính n1 / n2.
#Tính n1 // n2.
#Tính n1 % n2.
class Number:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __floordiv__(self, other):
        return Number(self.value // other.value)

    def __mod__(self, other):
        return Number(self.value % other.value)

    def __str__(self):
        return str(self.value)


n1 = Number(20)
n2 = Number(6)

#Bài 7: __len__, __getitem__
#Yêu cầu
# len(lst) để lấy số phần tử.
#Lấy phần tử ở vị trí 0.
#Lấy phần tử ở vị trí 3.
#In ra phần tử cuối cùng bằng cú pháp lst[-1].

class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]


lst = MyList([10, 20, 30, 40, 50])

#Bài 8: __setitem__, __delitem__
#Yêu cầu
#Đổi phần tử ở vị trí 1 thành "sách".
#In lại store.
#Xóa phần tử ở vị trí 2.
#In lại store sau khi xóa.

class MyStore:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del self.items[key]

    def __str__(self):
        return str(self.items)


store = MyStore(['bút', 'vở', 'thước', 'tẩy'])
print(store)
