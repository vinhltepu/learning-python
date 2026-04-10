from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Định nghĩa model Goods cho bảng goods trong cơ sở dữ liệu
class Goods(db.Model):
    __tablename__ = 'goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

   