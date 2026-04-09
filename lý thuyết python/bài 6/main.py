
#bài tập 1 import mô-đun sys
#yêu cầu
#a nhập mô-đun sys
#b in ra danh sách đối số dòng lệnh
#c in ra phần tử đầu tiên của sys.argv

import sys

print(sys.argv)
print(sys.argv[0])
 

#bài tập 2 kiểm tra name
#yêu cầu
#a in ra giá trị của name
#b nếu chạy trực tiếp thì in thông báo
#c nếu được import thì in thông báo khác

print(__name__)

if __name__ == "main":
    print("module dang chay ")
else:
    print("module duoc import")


#bài tập 3 dùng from import
#yêu cầu
#a sử dụng from sys import argv
#b in ra toàn bộ argv
#c in ra số lượng phần tử trong argv

from sys import argv

print(argv)
print(len(argv))


#bài tập 4 dùng hàm dir
#yêu cầu
#a import mô-đun sys
#b dùng dir xem các thuộc tính của sys
#c tạo biến mới và dùng dir kiểm tra

import sys

print(dir(sys))

a = 10
print(dir())

#bài tập 5 xóa biến bằng del
#yêu cầu
#a tạo một biến
#b dùng dir kiểm tra
#c xóa biến bằng del và kiểm tra lại

x = 5
print(dir())
del x
print(dir())
