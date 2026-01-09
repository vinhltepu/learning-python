#bài 1 lớp circle

#yêu cầu
#tạo lớp circle
#có bán kính
#in ra bán kính

class Circle:
    def __init__(self, r):
        self.r = r

    def show(self):
        print(self.r)


c = Circle(7)
c.show()

#output
#7


#bài 2 lớp switch

#yêu cầu
#tạo lớp switch
#có phương thức on
#in ra trạng thái

class Switch:
    def on(self):
        print("switch on")


s = Switch()
s.on()


#output
#switch on


#bài 3 biến lớp counter

#yêu cầu
#tạo lớp counter
#có biến lớp total
#mỗi lần tạo đối tượng tăng total

class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1


a = Counter()
b = Counter()
c = Counter()

print(Counter.total)


#output
#3


#bài 4 kế thừa đơn giản

#yêu cầu
#tạo lớp base
#tạo lớp sub kế thừa base
#gọi phương thức lớp cha
class Base:
    def hello(self):
        print("hello base")


class Sub(Base):
    pass


s = Sub()
s.hello()


#output
#hello base


#bài 5 ghi đè phương thức

#yêu cầu
#tạo lớp parent
#tạo lớp child
#child ghi đè phương thức show
class Parent:
    def show(self):
        print("parent")


class Child(Parent):
    def show(self):
        print("child")


c = Child()
c.show()


#output
#child


#bài 6 đa hình cơ bản

#yêu cầu
#hai lớp có cùng phương thức run
#gọi run bằng vòng lặp

class One:
    def run(self):
        print("run one")


class Two:
    def run(self):
        print("run two")


items = [One(), Two()]

for i in items:
    i.run()


#output
#run one
#run two