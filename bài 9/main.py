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



#Bài 7

#Đề bài
#Tạo lớp HọcSinh
#Có tên và tuổi
#Hiển thị thông tin

class HocSinh:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def hien_thi(self):
        print(self.ten, self.tuoi)

hs = HocSinh("Vinh", 20)
hs.hien_thi()

#Output
#Vinh 20 

#Bài 8

#Đề bài
#Tạo lớp HìnhChữNhật
#Có chiều dài, chiều rộng
#Tính diện tích

class HinhChuNhat:
    def __init__(self, d, r):
        self.d = d
        self.r = r

    def dien_tich(self):
        print(self.d * self.r)

h = HinhChuNhat(4, 5)
h.dien_tich()


#Output
#20

#Bài 9

#Đề bài
#Tạo lớp Xe
#Có hãng xe
#In hãng xe

class Xe:
    def __init__(self, hang):
        self.hang = hang

    def hien_thi(self):
        print(self.hang)

x = Xe("Honda")
x.hien_thi()


#Output
#Honda

#Bài 10

#Đề bài
#Tạo lớp Sách
#Có tên sách và giá
#In thông tin

class Sach:
    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia

    def thong_tin(self):
        print(self.ten, self.gia)

s = Sach("Python", 50000)
s.thong_tin()


#Output
#Python 50000

#Bài 11

#Đề bài
#Tạo lớp SinhVien
#Có tên và điểm
#In điểm
class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

    def hien_thi(self):
        print(self.diem)

sv = SinhVien("Vinh", 8)
sv.hien_thi()
#Output
#8

#Bài 12

#Đề bài
#Tạo lớp MayTinh
#Có thuộc tính tên máy
#Có phương thức hiển thị tên máy

class MayTinh:
    def __init__(self, ten):
        self.ten = ten

    def hien_thi(self):
        print(self.ten)

mt = MayTinh("Victus")
mt.hien_thi()

#Output
#Victus

#Bài 13
#Đề bài
#Tạo lớp HinhVuong
#Có thuộc tính cạnh
#Tính và in diện tích

class HinhVuong:
    def __init__(self, canh):
        self.canh = canh

    def dien_tich(self):
        print(self.canh * self.canh)

hv = HinhVuong(4)
hv.dien_tich()


#Output
#16

#Bài 14
#Đề bài
#Tạo lớp TaiKhoanNganHang
#Có số dư ban đầu
#In số dư tài khoản

class TaiKhoanNganHang:
    def __init__(self, so_du):
        self.so_du = so_du

    def xem_so_du(self):
        print(self.so_du)

tk = TaiKhoanNganHang(5000)
tk.xem_so_du()

#Output
#5000

#Bài 15

#Đề bài
#Tạo lớp QuatDien
#Có thuộc tính mức gió
#In mức gió hiện tại

class QuatDien:
    def __init__(self, muc_gio):
        self.muc_gio = muc_gio

    def hien_thi(self):
        print(self.muc_gio)

q = QuatDien(2)
q.hien_thi()


#Output
#2

#Bài 16
#Đề bài
#Tạo lớp MonAn
#Có tên món ăn
#In thông báo đang ăn món đó

class MonAn:
    def __init__(self, ten):
        self.ten = ten

    def an(self):
        print("Đang ăn", self.ten)

m = MonAn("Cơm")
m.an()

#Output
#Đang ăn Cơm

#Bài 17
#Đề bài
#Tạo lớp DongVat
#Có thuộc tính tên
#In tên động vật

class DongVat:
    def __init__(self, ten):
        self.ten = ten

    def hien_thi(self):
        print(self.ten)

dv = DongVat("Hổ")
dv.hien_thi()


#Output
#Hổ