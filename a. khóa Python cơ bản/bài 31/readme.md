# Special Methods trong Python 
Các special methods (hay còn gọi là magic methods hoặc dunder methods) là các phương thức đặc biệt có tên bắt đầu
kết thúc bằng hai dấu gạch dưới (__). Những phương thức này cho phép bạn "giao tiếp" trực tiếp với hệ thống hoặc thao
tác với các hành động cơ bản trong Python, như phép toán, so sánh, và tương tác với các đối tượng.

Special methods không được gọi trực tiếp từ người dùng, mà chúng sẽ được gọi tự động khi bạn thực hiện các thao tác
đặc biệt.

#  1. Khởi tạo và xây dựng đối tượng
__init__(self): Phương thức khởi tạo (constructor). Được gọi khi một đối tượng được tạo ra.

__del__(self): Phương thức hủy (destructor). Được gọi khi đối tượng bị hủy (tuy nhiên, không phải lúc nào cũng đảm bảo). 
def __del__(self):
   print(self.get_fullname(), "Đã bị hủy")

# 2. Chuỗi và Biểu diễn đối tượng
__str__(self): Trả về chuỗi mô tả ngắn gọn của đối tượng, được sử dụng khi bạn in đối tượng ra màn hình (ví dụ: print()).
def __str__(self):
    return f'Nhân viên có tên là: {self.get_fullname()}'

__repr__(self): Trả về chuỗi mô tả chính thức của đối tượng, thường dùng cho debugging, có thể sao chép và dán lại vào Python để tái tạo đối tượng.

def __repr__(self):
    return f'Employee({self.first_name}, {self.last_name}, {self.age}, {self.address}, {self.salary})'

# 3. So sánh đối tượng
__eq__(self, other): Kiểm tra sự bằng nhau (==).
__ne__(self, other): Kiểm tra sự không bằng nhau (!=).
__lt__(self, other): Kiểm tra nhỏ hơn (<).
__le__(self, other): Kiểm tra nhỏ hơn hoặc bằng (<=).
__gt__(self, other): Kiểm tra lớn hơn (>).
__ge__(self, other): Kiểm tra lớn hơn hoặc bằng (>=).

# 4. Phép toán
__add__(self, other): Phương thức gọi khi sử dụng toán tử cộng (+).
__sub__(self, other): Phương thức gọi khi sử dụng toán tử trừ (-).
__mul__(self, other): Phương thức gọi khi sử dụng toán tử nhân (*).
__truediv__(self, other): Phương thức gọi khi sử dụng toán tử chia (/).
__floordiv__(self, other): Phương thức gọi khi sử dụng toán tử chia lấy phần nguyên (//).
__mod__(self, other): Phương thức gọi khi sử dụng toán tử chia lấy dư (%).
__pow__(self, other): Phương thức gọi khi sử dụng toán tử lũy thừa (**).

# 5. Chuyển đổi kiểu và ép kiểu
__len__(self): Được gọi khi bạn sử dụng hàm len().
__getitem__(self, key): Được gọi khi bạn truy cập phần tử của đối tượng như là một danh sách (sử dụng dấu ngoặc vuông []).
__setitem__(self, key, value): Được gọi khi bạn gán giá trị cho phần tử của đối tượng (sử dụng dấu ngoặc vuông []).
__delitem__(self, key): Được gọi khi bạn xóa phần tử trong đối tượng (sử dụng del).