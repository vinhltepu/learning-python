#bài 1 nhập và xuất dữ liệu cơ bản
#yêu cầu
#nhập tên người dùng từ bàn phím
#nhập tuổi người dùng
#in ra câu chào kèm tên và tuổi

name = input("nhap ten: ")
age = input("nhap tuoi: ")
print("xin chao", name)
print("ban", age, "tuoi")

#output

#nhap ten: vinh
#nhap tuoi: 20
#xin chao vinh
#ban 20 tuoi


#bài 2 tính tổng hai số
#yêu cầu
#nhập số nguyên a
#nhập số nguyên b
#in ra tổng a + b

a = int(input("nhap a: "))
b = int(input("nhap b: "))
tong = a + b
print("tong =", tong)

#output
#nhap a: 4
#nhap b: 6
#tong = 10


#bài 3 xử lý chuỗi
#yêu cầu
#nhập một chuỗi
#đảo ngược chuỗi đó
#in ra kết quả

s = input("nhap chuoi: ")
dao = s[::-1]
print(dao)


#output
#nhap chuoi: python
#nohtyp


#bài 4 kiểm tra số chẵn lẻ
#yêu cầu
#nhập một số nguyên
#kiểm tra số đó chẵn hay lẻ
#in ra kết quả

n = int(input("nhap so: "))
if n % 2 == 0:
    print("so chan")
else:
    print("so le")


#output
#nhap so: 7
#so le


#bài 5 ghi dữ liệu vào tệp
#yêu cầu
#nhập một dòng văn bản
#ghi nội dung đó vào file data.txt
#thông báo đã ghi xong

text = input("nhap noi dung: ")
f = open("data.txt", "w", encoding="utf-8")
f.write(text)
f.close()
print("da ghi vao tep")


#output
#nhap noi dung: hoc python
#da ghi vao tep


#bài 6 đọc dữ liệu từ tệp
#yêu cầu
#mở file data.txt
#đọc nội dung trong file
#in nội dung ra màn hình

f = open("data.txt", "r", encoding="utf-8")
content = f.read()
f.close()
print(content)

#output
#hoc python

#bài 7 kiểm tra chuỗi đối xứng đơn giản
#yêu cầu
#nhập một chuỗi
#đảo ngược chuỗi
#so sánh và in kết quả

s = input("nhap chuoi: ")
if s == s[::-1]:
    print("chuoi doi xung")
else:
    print("khong doi xung")


#output
#nhap chuoi: madam
#chuoi doi xung