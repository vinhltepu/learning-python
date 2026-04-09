#bài 1 truyền tuple và trả về nhiều giá trị

#đề bài
#1 viết hàm trả về tổng và hiệu của hai số
#2 sử dụng tuple để trả về nhiều giá trị
#3 gán kết quả trả về cho hai biến riêng biệt
#4 in kết quả ra màn hình

def calc(a, b):
    return a + b, a - b

tong, hieu = calc(10, 3)
print(tong)
print(hieu)


#output
#13
#7


#bài 2 list comprehension kết hợp điều kiện

#đề bài
#1 tạo một danh sách các số nguyên
#2 dùng list comprehension để lấy các số chẵn
#3 nhân đôi các số chẵn đó
#4 in danh sách mới

nums = [1, 2, 3, 4, 5, 6]
result = [i * 2 for i in nums if i % 2 == 0]
print(result)


#output
#[4, 8, 12]


#bài 3 mới lambda và list liên quan đến con vật

#đề bài
#1 tạo một danh sách các con vật, mỗi con vật gồm tên và số chân
#2 sử dụng lambda để sắp xếp danh sách theo số chân tăng dần
#3 không viết hàm def riêng, chỉ dùng lambda
#4 in danh sách sau khi sắp xếp

animals = [
    {"name": "cho", "legs": 4},
    {"name": "ga", "legs": 2},
    {"name": "ran", "legs": 0},
    {"name": "meo", "legs": 4}
]

animals.sort(key=lambda a: a["legs"])
print(animals)


#output
#[{'name': 'ran', 'legs': 0}, {'name': 'ga', 'legs': 2}, {'name': 'cho', 'legs': 4} {'name': 'meo', 'legs': 4}]


#bài 4 sử dụng *args trong hàm

#đề bài
#1 viết hàm nhận số lượng tham số bất kỳ
#2 tính tổng các số truyền vào
#3 sử dụng *args trong định nghĩa hàm
#4 in kết quả


def tong(*args):
    total = 0
    for i in args:
        total += i
    return total

print(tong(1, 2, 3))
print(tong(5, 10))


#output
#6
#15


#bài 5 assert và kiểm tra dữ liệu

#đề bài
#1 tạo một danh sách ban đầu
#2 dùng assert để kiểm tra danh sách không rỗng
#3 xóa phần tử cuối cùng của danh sách
#4 chạy lại assert để thấy lỗi
data = ["a"]
assert len(data) > 0
data.pop()
assert len(data) > 0


#output
#Traceback (most recent call last):
  #File "<stdin>", line 1, in <module>
#AssertionError
