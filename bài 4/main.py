#bài 1 dùng while và break
#yêu cầu
#nhập số nguyên
#dừng khi nhập 0
#in các số đã nhập

while True:
    n = int(input('Nhap so: '))
    if n == 0:
        break
    print(n)
 

#bài 2 dùng while và continue

#yêu cầu
#nhập số nguyên
#bỏ qua số âm
#in số dương

while True:
    n = int(input('Nhap so: '))
    if n < 0:
        continue
    if n == 0:
        break
    print(n)


#bài 3 dùng for và continue

#yêu cầu
#in số từ 1 đến 10
#bỏ qua số chẵn
##chỉ in số lẻ

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


#bài 4 dùng for và break
#yêu cầu
#in số từ 1 đến 10
#dừng khi gặp số 6
#không in số sau 6

for i in range(1, 11):
    if i == 6:
        break
    print(i)


#bài 5 kết hợp while, continue, break
#yêu cầu
#nhập chuỗi
#bỏ qua chuỗi ngắn hơn 3 ký tự
#dừng khi nhập quit

while True:
    s = input('Nhap chuoi: ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print(s)
