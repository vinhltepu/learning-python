from datetime import datetime
from sqlalchemy.exc import IntegrityError
from extensions import db
from models.product import Product, PaintingProduct, WoodProduct

class ProductService:
    def get_all(self, q: str | None = None):
        query = Product.query
        if q:
            like = f"%{q.strip()}%"
            query = query.filter((Product.name.ilike(like)) | (Product.code.ilike(like)))
        return query.order_by(Product.id.desc()).all()

    def get(self, pid: int):
        return Product.query.get(pid)

    def create_from_form(self, form):
        ptype = (form.get("product_type") or "base").strip().lower()

        cls = Product
        if ptype == "painting":
            cls = PaintingProduct
        elif ptype == "wood":
            cls = WoodProduct

        raw_date = (form.get("imported_date") or "").strip()
        try:
            imported_date = datetime.strptime(raw_date, "%Y-%m-%d").date()
        except:
            imported_date = datetime.today().date()

        p = cls(
            name=(form.get("name") or "").strip(),
            code=(form.get("code") or "").strip(),
            unit=(form.get("unit") or "").strip(),
            import_price=float(form.get("import_price") or 0),
            sell_price=float(form.get("sell_price") or 0),
            stock=int(form.get("stock") or 0),
            imported_date=imported_date,
        )

        p.paint_brand = (form.get("paint_brand") or "").strip() or None
        p.wood_source = (form.get("wood_source") or "").strip() or None

        p.validate()
        return p

    def add(self, product: Product):
        try:
            db.session.add(product)
            db.session.commit()
            return product
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Mã hàng hóa đã tồn tại (bị trùng).")

    def update_from_form(self, product: Product, form):
        product.name = (form.get("name") or "").strip()
        product.code = (form.get("code") or "").strip()
        product.unit = (form.get("unit") or "").strip()
        product.import_price = float(form.get("import_price") or 0)
        product.sell_price = float(form.get("sell_price") or 0)
        product.stock = int(form.get("stock") or 0)

        raw_date = (form.get("imported_date") or "").strip()
        if raw_date:
            try:
                product.imported_date = datetime.strptime(raw_date, "%Y-%m-%d").date()
            except:
                pass

        product.product_type = (form.get("product_type") or product.product_type or "base").strip().lower()
        product.paint_brand = (form.get("paint_brand") or "").strip() or None
        product.wood_source = (form.get("wood_source") or "").strip() or None

        product.validate()

        try:
            db.session.commit()
            return product
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Mã hàng hóa bị trùng.")

    def delete(self, product: Product):
        db.session.delete(product)
        db.session.commit()