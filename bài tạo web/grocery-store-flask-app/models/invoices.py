from datetime import datetime 
from app import db    
# lấy ngàu và giờ hiện tại để lưu vào cột created_at khi tạo hóa đơn mới
class Invoice(db.Model):
    __tablename__ = 'invoices'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    subtotal = db.Column(db.Float, default=0)
    discount_rate = db.Column(db.Float, default=0)
    total_amount = db.Column(db.Float, default=0)

    details = db.relationship("InvoiceDetail", backref="invoice")
 
def calculate_total(self): # tính tổng tiền hóa đơn và giảm giá  dựa trên chi tiêu 
    self.subtotal = sum(detail.line_total for detail in self.details)
    self.discount_rate = self.customer.get_discount_rate() # lấy tỷ lệ giảm giá 
    self.total_amount = self.subtotal * (1 - self.discount_rate) # tính tổng khi áp dụng mã 
    return self.total_amount

@classmethod # phương thức lớp để tính doanh thu theo ngày
def revenue_by_day(cls): # truy vấn cơ sở dữ liệu để tính tổng doanh thu theo ngày
    result = db.session.query( 
        db.func.date(cls.created_at), # lấy ngày từ cột created_at
        db.func.sum(cls.total_amount) # tính tổng doanh thu trong ngày đó
    ).group_by( # nhóm kết quả theo ngày
        db.func.date(cls.created_at)# nhóm theo ngày từ cột created_at
    ).all()

    return result

def show_invoice_info(self):
    return "invoice " + str(self.id) + " customer " + str(self.customer_id)
