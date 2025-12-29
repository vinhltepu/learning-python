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