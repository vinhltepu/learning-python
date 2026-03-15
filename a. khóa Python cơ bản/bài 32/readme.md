# Property, Getter, Setter và Deleter trong Python 
property là một decorator trong Python, cho phép bạn chuyển đổi một phương thức (method) thành một thuộc tính
(property) mà không cần phải gọi nó như một hàm.

class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property // biến một method thành một thuộc tính
    def fullname(self):
        print('Method fullname is running')
        return f"{self.first_name} - {self.last_name}"


emp = Employee('Nguyen', 'Tam')

print(emp.fullname)

# - Khái niệm "encapsulation": Python không có tính năng private thật sự (như các ngôn ngữ khác), việc đặt tên thuộc
tính bắt đầu bằng dấu gạch dưới _ là một cách để cho biết thuộc tính đó chỉ nên được sử dụng trong lớp, không phải từ
bên ngoài (Đây chỉ là một quy ước, nhưng nó giúp bạn làm rõ ràng hơn về mục đích của các thuộc tính).

class Employee:

    def __init__(self, first_name, last_name): //đây là hàm khởi tạo, chạy khi  tạo object mới từ lớp Employee.
        self.first_name = first_name 
        self.last_name = last_name
        self._email = f"{first_name}.{last_name}@gmail.com" // tạo email mặc định theo định dạng

    # getter => lấy
    @property
    def email(self):
        'Day la ghi chú nhe'
        return f"Đây là 1 email: {self._email}"

    # setter => thiết lập
    @email.setter
    def email(self, new_email):
        self._email = new_email
    
    # deleter
    @email.deleter
    def email(self):
        self._email = 'Đã xóa email đi rồi'


emp = Employee('Nguyen', 'Tam')

emp._email = 'a@gmail.com'

print(emp.email)