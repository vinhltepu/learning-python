# Chuỗi JSON và Module JSON – Tạo, Chuyển Đổi, và Lưu Trữ Dữ Liệu

JSON (JavaScript Object Notation)
JSON là một định dạng dữ liệu nhẹ, dễ đọc và viết, thường dùng để trao đổi dữ liệu giữa server và client hoặc lưu
dữ liệu. Nó có cấu trúc dạng cặp key-value (Chuỗi JSON)

# Tác dụng:
1. Trao đổi dữ liệu giữa client và server
2. Lưu trữ dữ liệu cấu hình
3. Lưu trữ dữ liệu thay thế cho database nhỏ
4. Chuyển đổi dữ liệu giữa các ngôn ngữ lập trình
5. Dùng trong Web và Mobile App 

# Nếu JSON là một đối tượng -> Bắt đầu bằng {}
# Nếu JSON là một danh sách -> Bắt đầu bằng []

# JSON        Python
# object {}   dict (dictionary)
# array []    list (danh sách)
# string "text"  str (chuỗi)
# number 123     int hoặc float
# true / false   True / False
# null           None

# Các key và chuỗi str thì nó sẽ phải được bọc hoặc để vào trong dấu nháy đôi ""

## Quy tắc JSON quan trọng:
# Dữ liệu phải nằm trong {} nếu là object.
# Key (tên thuộc tính) luôn phải đặt trong dấu "".
# Các phần tử trong array nằm trong [].
# Phải dùng , để phân cách giữa các phần tử, nhưng không có dấu , sau phần tử cuối cùng.

# cú pháp tạo chuỗi json
json_data = """
{
    "name": "Nguyen A",
    "age": 19,
    "email": ["t@gmail.com", "tedu@edu.vn"]
    "rich": false,
    "demo": null
}
"""

# chuyển chuỗi jison thành dữ liệu python 
import json

# loads function => để chuyển kiểu dữ liệu json -> kiểu dữ liệu python
data_python: dict =  json.loads(json_data)

# xử lý dữ liệu json 
print(type(data_python['name']))

# chuyển đổi kiểu dữ liệu bên python => chuỗi json
# dump => xuất ra, đổ ra
# s => string
data_json = json.dumps(data_python, ensure_ascii=False)

print(data_json)

# Đọc dữ liệu json từ 1 file lên chương trình python
with open('users.json', encoding='utf-8') as file:
    data_json = json.load(file)

print(data_json)
# Muốn in name, email, city của tất cả các users có trong list
# Lấy name ra trước
for user in data_json:
    print(f"Username: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"City: {user['address']['city']}")
    print()
# Tạo dữ liệu:

data.append({
    "Username": user['name'],
    "Email": user['email'],
    "City": user['address']['city']
})

# Muốn in dữ liệu json ra 1 file

with open('new_users.json', 'w', encoding='utf-8') as write_file:
    json.dump(obj=)