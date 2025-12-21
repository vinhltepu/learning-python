 #(Bài 1: Toán tử số học
#Đề bài:
#Viết chương trình nhập vào 2 số nguyên a và b.
#In ra:
#Tổng của a và b
#Hiệu của a và b
#Tích của a và b
#Thương nguyên của a chia b
#Phần dư của a chia b )


a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)


#(Bài 2: Toán tử so sánh
#đề bài:
#Nhập hai số nguyên x và y.
#In ra kết quả của các phép so sánh:
#x > y
#x < y
#x == y
# x != y
#x >= y)
 

x = int(input())
y = int(input())

print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)


#(Bài 3: Toán tử logic
#Đề bài:
#Nhập hai giá trị logic c và d (True hoặc False).
#In ra kết quả của:
#c and d
#c or d
#not c
#not d
#(c and d) or c)

c = bool(input())
d = bool(input())

print(c and d)
print(c or d)
print(not c)
print(not d)
print((c and d) or c)



#(Bài 4: Toán tử lũy thừa và chia
#Đề bài:
#Nhập hai số nguyên m và n.
#In ra:
#m mũ n
#n mũ m
#Thương chia thực của m cho n
#thương nguyên của m cho n
#Phần dư của m chia n

m = int(input())
n = int(input())

print(m ** n)
print(n ** m)
print(m / n)
print(m // n)
print(m % n)


#Bài 5: Kết hợp toán tử
##Đề bài:
#Nhập 2 số nguyên e và f .
#In ra:
#Tổng e + f
#Kiểm tra e có chia hết cho f không
#Kiểm tra e có lớn hơn 10 và f nhỏ hơn 5 không
#Liệu tuyệt đối của e và f
#Giá trị lớn hơn giữa e và f


e = int(input())
f = int(input())

print(e + f)
print(e % f == 0)
print(e > 10 and f < 5)
print(abs(e - f))
print(max(e, f))
