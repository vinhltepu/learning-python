from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.goods import Product, PaintingProduct, WoodProduct
from datetime import datetime

goods_bp = Blueprint("goods", __name__)


@goods_bp.route("/")
def list_goods():
    keyword = request.args.get("keyword", "").strip()

    if keyword:
        products = Product.query.filter(
            (Product.name.contains(keyword)) |
            (Product.code.contains(keyword))
        ).all()
    else:
        products = Product.query.all()

    return render_template("goods.html", products=products, keyword=keyword)


@goods_bp.route("/add", methods=["POST"])
def add_goods():
    product_type = request.form.get("product_type")
    name = request.form.get("name")
    code = request.form.get("code")
    unit = request.form.get("unit")
    import_price = request.form.get("import_price")
    sale_price = request.form.get("sale_price")
    stock = request.form.get("stock")
    import_date = request.form.get("import_date")

    try:
        import_price = float(import_price)
    except (ValueError, TypeError):
        import_price = 0.0

    try:
        sale_price = float(sale_price)
    except (ValueError, TypeError):
        sale_price = 0.0

    try:
        stock = int(stock)
    except (ValueError, TypeError):
        stock = 0

    try:
        import_date = datetime.strptime(import_date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        import_date = datetime.now().date()

    if product_type == "painting":
        brand_name = request.form.get("brand_name") or ""
        product = PaintingProduct(
            name=name,
            code=code,
            unit=unit,
            import_price=import_price,
            sale_price=sale_price,
            stock=stock,
            import_date=import_date,
            brand_name=brand_name
        )
    elif product_type == "wood":
        source = request.form.get("source") or ""
        product = WoodProduct(
            name=name,
            code=code,
            unit=unit,
            import_price=import_price,
            sale_price=sale_price,
            stock=stock,
            import_date=import_date,
            source=source
        )
    else:
        product = Product(
            name=name,
            code=code,
            unit=unit,
            import_price=import_price,
            sale_price=sale_price,
            stock=stock,
            import_date=import_date
        )

    db.session.add(product)
    db.session.commit()

    flash("Thêm hàng hóa thành công", "success")
    return redirect(url_for("goods.list_goods"))


@goods_bp.route("/edit/<int:product_id>", methods=["GET", "POST"])
def edit_goods(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == "POST":
        product.name = request.form.get("name")
        product.code = request.form.get("code")
        product.unit = request.form.get("unit")

        try:
            product.import_price = float(request.form.get("import_price"))
        except (ValueError, TypeError):
            product.import_price = 0.0

        try:
            product.sale_price = float(request.form.get("sale_price"))
        except (ValueError, TypeError):
            product.sale_price = 0.0

        try:
            product.stock = int(request.form.get("stock"))
        except (ValueError, TypeError):
            product.stock = 0

        try:
            product.import_date = datetime.strptime(request.form.get("import_date"), "%Y-%m-%d").date()
        except (ValueError, TypeError):
            product.import_date = datetime.now().date()

        if hasattr(product, "brand_name"):
            product.brand_name = request.form.get("brand_name") or product.brand_name
        if hasattr(product, "source"):
            product.source = request.form.get("source") or product.source

        db.session.commit()
        flash("Cập nhật hàng hóa thành công", "success")
        return redirect(url_for("goods.list_goods"))

    return render_template("edit_goods.html", product=product)


@goods_bp.route("/delete/<int:product_id>", methods=["POST"])
def delete_goods(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()

    flash("Xóa hàng hóa thành công", "success")
    return redirect(url_for("goods.list_goods"))
