#bài 1 hàm đơn giản
#yêu cầu
#tạo một hàm in ra hello
#gọi hàm 1 lần
#có docstring
  
def hello():
    """in ra hello"""
    print("hello")

hello()


#bài 2 hàm có tham số
#yêu cầu
#viết hàm nhận 2 số
#in ra tổng 2 số đó
#gọi hàm với số cụ thể

def tong(a, b):
    print(a + b)

tong(3, 5)

#bài 3 tham số mặc định
#yêu cầu
#iết hàm in chữ
#nếu không truyền số lần thì in 1 lần
#gọi hàm 2 cách

def in_chu(chu, lan=1):
    print(chu * lan)

in_chu("hi")
in_chu("ok", 3)


#bài 4 biến global
#yêu cầu
#tạo biến x bên ngoài
#viết hàm đổi giá trị x
#in x trước và sau

x = 5

def doi_x():
    global x
    x = 10

print(x)
doi_x()
print(x)


#bài 5 return và varargs
#yêu cầu
#viết hàm nhận nhiều số
#trả về tổng
#in kết quả

def tinh_tong(*so):
    tong = 0
    for i in so:
        tong += i
    return tong

print(tinh_tong(1, 2, 3))

