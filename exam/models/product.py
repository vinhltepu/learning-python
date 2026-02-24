from datetime import date
from extensions import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(100), nullable=False, unique=True)
    unit = db.Column(db.String(50), nullable=False)

    import_price = db.Column(db.Float, nullable=False, default=0)
    sell_price = db.Column(db.Float, nullable=False, default=0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    imported_date = db.Column(db.Date, nullable=False, default=date.today)

    product_type = db.Column(db.String(50), nullable=False, default="base")
    paint_brand = db.Column(db.String(255), nullable=True)
    wood_source = db.Column(db.String(255), nullable=True)

    __mapper_args__ = {
        "polymorphic_on": product_type,
        "polymorphic_identity": "base",
    }

    def validate(self):
        if not self.name or not self.code or not self.unit:
            raise ValueError("Vui lòng nhập đủ: Tên, Mã, Đơn vị.")
        if self.import_price < 0 or self.sell_price < 0:
            raise ValueError("Giá không được âm.")
        if self.sell_price < self.import_price:
            raise ValueError("Giá bán phải >= giá nhập.")
        if self.stock < 0:
            raise ValueError("Tồn kho không được âm.")

class PaintingProduct(Product):
    __mapper_args__ = {"polymorphic_identity": "painting"}

class WoodProduct(Product):
    __mapper_args__ = {"polymorphic_identity": "wood"}