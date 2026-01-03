#BÀI 1: List và Sequence
#Yêu cầu

#a) Tạo một list chứa 4 số nguyên
#b) In ra độ dài của list
#c) In ra phần tử đầu tiên
#d) In ra phần tử cuối cùng

numbers = [2, 4, 6, 8]

print(len(numbers))
print(numbers[0])
print(numbers[-1])

# 4
#2
#8



#BÀI 2: Tuple
#Yêu cầu
#a) Tạo một tuple chứa 3 ngày trong tuần
#b) In ra tuple đó
#c) In ra số lượng phần tử
#d) In ra phần tử thứ 2


days = ("thu2", "thu3", "thu4")

print(days)
print(len(days))
print(days[1])

#ouput
#('thu2', 'thu3', 'thu4')
#3
#thu3

#Bài 3: Tuple + Sequence + Indexing
#Yêu cầu

#a) Tạo một tuple chứa tên các thành phố
#b) In ra số lượng phần tử trong tuple
#c) In ra phần tử cuối cùng của tuple

cities = ('hanoi', 'thaibinh', 'binhduong', 'saigon')
print(len(cities))
print(cities[-1])
#ouput 
#4
#saigon

#Bài 3: Dictionary + Sequence + Loop
#Yêu cầu

#a) Tạo một từ điển lưu tên và điểm số
#b) Thêm một học sinh mới vào từ điển
#c) Duyệt và in toàn bộ cặp khóa – giá trị

scores = {
    'ban 1 ': 8,
    'ban 2 ': 7
}

scores['ban 3 '] = 9

for name, score in scores.items():
    print(name, score)
#ouput
#ban 1 8
#ban 2 7
#ban 3 9



#BÀI 4: Tuple + Sequence
#Yêu cầu

#a) Tạo tuple chứa 5 số bất kỳ
#b) In ra tuple
#c) In ra 3 phần tử đầu tiên
#d) Kiểm tra số 10 có nằm trong tuple hay không

numbers = (3, 5, 7, 9, 10)

print(numbers)
print(numbers[:3])
print(10 in numbers)

# Output
#(3, 5, 7, 9, 10)
#(3, 5, 7)
#True



#BÀI 5: List + Indexing
#Yêu cầu

#a) Tạo list gồm 5 màu sắc
#b) In phần tử đầu tiên
#c) In phần tử cuối cùng
#d) In toàn bộ list

colors = ["do", "xanhduong", "xanhlacay", "vang", "den"]

print(colors[0])
print(colors[-1])
print(colors)

#Output
#do
#den
#['do', 'xanhduong', 'xanhlacay', 'vang', 'den']



#BÀI 6: Copy List bằng slicing
#Yêu cầu

#a) Tạo list
#b) Sao chép list
#c) Xóa phần tử list mới
#d) In hai list

a = [1, 2, 3]
b = a[:]

del b[0]

print(a)
print(b)

#Output
#[1, 2, 3]
#[2, 3]

#BÀI 7: Dictionary + keys
#Yêu cầu

#a) Tạo dictionary điểm
#b) In toàn bộ key
#c) In toàn bộ value
#d) In dictionary

scores = {"toan": 8, "hoa": 9}

print(scores.keys())
print(scores.values())
print(scores)

#Output
#dict_keys(['toan', 'hoa'])
#dict_values([8, 9])
#{'toan': 8, 'hoa': 9}


#BÀI 8: More About Strings
#Yêu cầu

#a) Tạo chuỗi
#b) Tìm vị trí chữ "o"
#c) In kết quả
#d) Giải thích kết quả

word = "Hello"

print(word.find("o"))
print("Vi tri chu o")

#Output
#4
#Vi tri chu o



#Bài 9: List + Sequence + Index + Slicing
#Yêu cầu

#Tạo một danh sách màu sắc.
#In ra màu đầu tiên và màu cuối cùng.
#Cắt lấy 3 màu đầu tiên trong danh sách.
#In toàn bộ danh sách.

colors = ["do", "xanhduong", "xanhlacay", "vang", "den", "trang"]

print("Mau dau tien:", colors[0])
print("Mau cuoi cung:", colors[-1])
print("Ba mau dau:", colors[:3])
print("Tat ca mau:", colors)

#Output
#Mau dau tien: do
#Mau cuoi cung: trang
#Ba mau dau: ['do', 'xanhduong', 'xanhlacay']
#Tat ca mau: ['do', 'xanhduong', 'xanhlacay', 'vang', 'den', 'trang']


#Bài 10: Tuple + Index + Bat bien
#Yêu cầu

#Tạo tuple chứa các màu sắc.
#In số lượng màu trong tuple.
#Truy cập màu thứ 2.
#Thử thay đổi một phần tử (quan sát lỗi).


colors = ("do", "xanhduong", "vang", "den")

print("So luong mau:", len(colors))
print("Mau thu 2:", colors[1])

#Output
#So luong mau: 4
#Mau thu 2: xanhduong

#Bài 11: List + in + len
#Yêu cầu

#Tạo danh sách màu sắc.
#Kiểm tra xem màu "do" có trong danh sách không.
#In số lượng màu.
#In toàn bộ danh sách.

colors = ["do", "vang", "xanhduong", "den"]

print("Co mau do khong:", "do" in colors)
print("So luong mau:", len(colors))
print("Danh sach mau:", colors)

#Output
#Co mau do khong: True
#So luong mau: 4
#Danh sach mau: ['do', 'vang', 'xanhduong', 'den']



#Bai 12: Danh sach mon hoc (List + len + in)
#Yeu cau

#Tao danh sach mon hoc.
#Kiem tra mon "toan" co trong danh sach khong.
#In so mon hoc.
#In toan bo danh sach.

subjects = ["toan", "ly", "hoa", "tin"]

print("Co mon toan khong:", "toan" in subjects)
print("So mon hoc:", len(subjects))
print("Danh sach mon hoc:", subjects)

#Output
#Co mon toan khong: True
#So mon hoc: 4
#Danh sach mon hoc: ['toan', 'ly', 'hoa', 'tin']


#Bai 13: Tuple thong tin sinh vien
#Yeu cau
#Tao tuple thong tin sinh vien.
#In toan bo thong tin.
#Truy cap ten sinh vien.
#Truy cap nam sinh.

student = ("Vinh", 2005, "DTVT")

print(student)
print("Ten:", student[0])
print("Nam sinh:", student[1])

#Output
#('Vinh', 2005, 'DTVT')
#Ten: Vinh
#Nam sinh: 2005


#Bai 14: Dictionary diem so
#Yeu cau
#Tao tu dien mon hoc va diem.
#In diem mon toan.
#Kiem tra mon tin co trong tu dien khong.
#In so mon hoc.

scores = {
    "toan": 8,
    "ly": 7,
    "hoa": 9
}

print("Diem toan:", scores["toan"])
print("Co mon tin khong:", "tin" in scores)
print("So mon:", len(scores))

#Output
#Diem toan: 8
#Co mon tin khong: False
#So mon: 3


#Bai 15: Sequence + slicing (Danh sach so)
#Yeu cau
#Tao danh sach so.
#Lay 3 so dau.
#Lay 2 so cuoi.
#Dao nguoc danh sach.

numbers = [1, 2, 3, 4, 5, 6]

print("Ba so dau:", numbers[:3])
print("Hai so cuoi:", numbers[-2:])
print("Dao nguoc:", numbers[::-1])

#Output
#Ba so dau: [1, 2, 3]
#Hai so cuoi: [5, 6]
#Dao nguoc: [6, 5, 4, 3, 2, 1]


#Bai 16: String + startswith + find
#Yeu cau
#Tao chuoi ten.
#Kiem tra bat dau bang ky tu "thanh".
#Tim vi tri chuoi con.
#In ket qua.

name = "thanhvinh"

print(name.startswith("thanh"))
print(name.find("vinh"))

#Output
#True
#5

#Bai 7: Join + List + String
#Yeu cau
#Tao danh sach thanh pho.
#Noi cac phan tu bang dau -.
#In chuoi moi.
#In kieu du lieu.

cities = ["HaNoi", "DaNang", "SaiGon"]

result = " - ".join(cities)

print(result)
print(type(result))

#Output
#HaNoi - DaNang - SaiGon
#<class 'str'>