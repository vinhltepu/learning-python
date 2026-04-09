from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Định nghĩa model Customer cho bảng customers trong cơ sở dữ liệu
class Customer(db.Model):
    __tablename__ = 'customers'
    # các cột trong bảng customers
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

