from datetime import date
from extensions import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    import_price = db.Column(db.Float, nullable=False)
    sale_price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    import_date = db.Column(db.Date, default=date.today)

    __mapper_args__ = { # thiết lập phân loại sản phẩm dựa trên cột type
        "polymorphic_identity": "product", # định danh cho class gốc là "product"
        "polymorphic_on": type
    }

    def __init__(self, name, code, unit, import_price, sale_price, stock, import_date=None): # hàm khởi tạo sản phẩm mới, nếu import_date không được cung cấp sẽ mặc định là ngày hiện tại
        self.name = name
        self.code = code
        self.unit = unit
        self.import_price = import_price
        self.sale_price = sale_price
        self.stock = stock
        self.import_date = import_date if import_date else date.today()

    def show_product_info(self): # hiển thị thông tin sản phẩm, có thể được ghi đè trong các lớp con để hiển thị thêm thông tin đặc thù
        return f"{self.code} - {self.name} - Tồn kho: {self.stock}"


class PaintingProduct(Product): #sản phẩm sơn kế thừa từ product
    __tablename__ = "painting_products" # tên bảng trong cơ sở dữ liệu cho sản phẩm sơn

    id = db.Column(db.Integer, db.ForeignKey("products.id"), primary_key=True) # cột id là khóa chính và cũng là khóa ngoại liên kết với bảng products
    brand_name = db.Column(db.String(100), nullable=False) # cột brand_name để lưu tên hãng sơn và  không được để trống
 
    __mapper_args__ = {
        "polymorphic_identity": "painting" # định danh cho class con là "painting"
    }

    def __init__(self, name, code, unit, import_price, sale_price, stock, brand_name, import_date=None):#hàm khởi tạo sản phẩm mới 
        super().__init__(name, code, unit, import_price, sale_price, stock, import_date) # gọi hàm khởi tạo của lớp cha để thiết lập các thuộc tính chung
        self.brand_name = brand_name # thiết lập thuộc tính riêng của sản phẩm sơn là tên hãng sơn

    def show_product_info(self): 
        return f"{self.code} - {self.name} - Hãng sơn: {self.brand_name}"


class WoodProduct(Product):
    __tablename__ = "wood_products"

    id = db.Column(db.Integer, db.ForeignKey("products.id"), primary_key=True)
    source = db.Column(db.String(150), nullable=False)

    __mapper_args__ = {    # định danh cho class con là "wood"
        "polymorphic_identity": "wood"
    }

    def __init__(self, name, code, unit, import_price, sale_price, stock, source, import_date=None):#   hàm khởi tạo sản phẩm mới
        super().__init__(name, code, unit, import_price, sale_price, stock, import_date)
        self.source = source

    def show_product_info(self): # ghi đè phương thức hiển thị thông tin sản phẩm để bao gồm nguồn gỗ
        return f"{self.code} - {self.name} - Nguồn nhập: {self.source}"