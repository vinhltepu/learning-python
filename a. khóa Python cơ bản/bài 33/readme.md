#  Duck Typing và Nguyên Tắc 'Asking Forgiveness, Not Permission' 

Duck Typing: Đây là một khái niệm trong lập trình, mô tả cách mà một đối tượng được xử lý dựa trên hành vi của nó vì loại của đối tượng đó.

class Cat:
    def sleep(self):
        print('Cat is sleeping ')

    def eat(self):
        print('Cat is eating ')

class Dog:
    def sleep(self):
        print('Dog is sleeping ')

    def eat(self):
        print('Dog is eating ')

class Duck():
    pass


def check_method(thing):
    if isinstance(thing, Cat) or isinstance(thing, Dog):
        thing.sleep()
        thing.eat()
    else:
        print('Not Cat') 


c = Cat()
d = Dog()

# check_method(d)
check_method(Duck())

# "Asking Forgiveness, Not Permission (EAFP)" – "Hỏi sự tha thứ, không phải sự cho phép"
Đây là một nguyên tắc lập trình, nói rằng bạn nên giả định rằng mọi thứ sẽ diễn ra đúng và chỉ xử lý lỗi khi chúng xảy ra, thay vì kiểm tra điều kiện trước để tránh lỗi.

# vd 
list_numbers = [5, 10, 15]

index = 10

try:
    print(list_numbers[index])
except Exception:
    print('Error: index') 
# vd 2 
dict_en = {'Hi': 'Xin chào'}

key = 'H'

try:
    print(dict_en[key])
except Exception:
    print('Lỗi thì vào đây')
