
from app import db
# Định nghĩa model Customer cho bảng customers trong cơ sở dữ liệu
class Customer(db.Model): # class để chế tạo model 
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True) # cột id là khóa chính
    type = db.Column(db.String(20), nullable=False) # cột type là chuỗi, có thể là 'individual' hoặc 'business'
    name = db.Column(db.String(100), nullable=False) # cột name là chuỗi
    phone = db.Column(db.String(20), nullable=False) # cột phone là chuỗi
    address = db.Column(db.String(200), nullable=False) # cột address là chuỗi
    total_spent = db.Column(db.Float, default=0.0) # cột total_spent là số thực, mặc định là 0.0

__mapper_args__ = {
    "polymorphic_identity": "customer", # class gốc là customer
    "polymorphic_on": type # phân biệt các loại khách hàng dựa trên cột type
}

invoices = db.relationship("Invoice", backref="customer", lazy=True) # hóa đơn và mối liên hệ với khách hàng , 1 khách hàng có thể có nhiều hóa đơn 


def __init__(self, name, phone, address, total_spent=0): # hàm khởi tạo khách hàng mới 
    self.name = name
    self.phone = phone
    self.address = address
    self.total_spent = total_spent

@property
def customer_name(self): # lấy tên khách hàng từ class customer
    return self.name  # hiển thị tên khách hàng 

@customer_name.setter
def set_customer_name(self, value):
    if value and len(value.strip()) >= 2:# kiểm tra tên khách hàng hợp lệ (ít nhất 2 ký tự)
        self.name = value.strip()
    else:
        raise ValueError("Invalid customer name. Name must be at least 2 characters long.") # đặt tên khách hàng, nếu tên không hợp lệ sẽ trả về lỗi

@property
def points(self): # tính điểm dựa trên chi tiêu 
        return self.total_spent  # trả về tổng số tiền đã chi

@points.setter
def points(self, new_points): # giá trị mới muốn cập nhật điểm tích lũy
    if float(new_points) >= 0: # kiểm tra >0 hay k
        self.total_spent = float(new_points) # cập nhật điểm 
    else:
        print("Điểm tích lũy không được âm")

@points.deleter
def points(self): # xóa điểm tích lũy và cho về 0 
    self.total_spent = 0

