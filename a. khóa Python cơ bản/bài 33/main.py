#Bài 1: Duck Typing với hành động của động vật
#4 ý cần hiểu
#Duck Typing quan tâm đến đối tượng làm được gì, không quá quan trọng nó thuộc class nào.
#Nếu một object có method phù hợp, ta có thể dùng nó.
#Không cần kiểm tra quá nhiều bằng isinstance().
#Cách này giúp code linh hoạt hơn.
#Đề bài
#Tạo 3 class:
#Cat có method sound()
#Dog có method sound()
#Duck có method sound()
#Viết hàm animal_sound(animal) để gọi sound().

class Cat:
    def sound(self):
        print('Meo meo')


class Dog:
    def sound(self):
        print('Gâu gâu')


class Duck:
    def sound(self):
        print('Cạp cạp')


def animal_sound(animal):
    animal.sound()


c = Cat()
d = Dog()
du = Duck()

animal_sound(c)
animal_sound(d)
animal_sound(du)

#Bài 2: EAFP với danh sách
#4 ý cần hiểu
#EAFP là cứ thử làm trước bằng try.
#Nếu lỗi xảy ra thì xử lý trong except.
#Không cần kiểm tra điều kiện trước quá nhiều.
#Rất hay dùng khi làm việc với list, dict, file,...
#Đề bài
#Cho một danh sách tên học sinh.
#Hãy in ra phần tử ở vị trí bất kỳ. Nếu vị trí không tồn tại thì báo lỗi.

students = ['A', 'B', 'C']

index = 1

try:
    print(students[index])
except Exception:
    print('Lỗi: vị trí không tồn tại')

#Bài 3: EAFP + Duck Typing đơn giản
#4 ý cần hiểu
#Ta có thể gọi method của object mà không cần kiểm tra class trước.
#Đây là tư duy gần với Duck Typing.
#Nếu object không có method cần thiết, ta bắt lỗi bằng try/except.
#Cách này vừa linh hoạt vừa dễ hiểu cho người mới học.
#Đề bài
#Tạo:
#Bird có method fly()
#Plane có method fly() 
#Fish không có method fly()
#Viết hàm start_fly(thing) để gọi fly(). Nếu không có method này thì báo lỗi.

class Bird:
    def fly(self):
        print('Bird is flying')


class Plane:
    def fly(self):
        print('Plane is flying')


class Fish:
    pass


def start_fly(thing):
    try:
        thing.fly()
    except Exception:
        print('Đối tượng này không thể bay')


b = Bird()
p = Plane()
f = Fish()

start_fly(b)
start_fly(p)
start_fly(f)