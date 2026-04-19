from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.goods import Product, PaintingProduct, WoodProduct
from datetime import datetime

goods_bp = Blueprint("goods", __name__)


@goods_bp.route("/") 
def list_goods(): # lấy từ khóa tìm kiếm, nếu có từ khóa thì tìm theo tên hoặc mã nếu không có thì lấy tất cả hàng hóa,gửi dữ liệu sang file goods.html
    keyword = request.args.get("keyword", "") # lấy từ khóa tìm kiếm từ tham số truy vấn, nếu không có thì gán giá trị mặc định là chuỗi rỗng
    keyword = keyword.strip()

    if keyword != "":
        products = Product.query.filter(
            (Product.name.contains(keyword)) |
            (Product.code.contains(keyword))
        ).all()
    else:
        products = Product.query.all()

    return render_template("goods.html", products=products, keyword=keyword)


@goods_bp.route("/add", methods=["POST"]) 
def add_goods(): # lấy dữ liệu từ form, chuyển đổi kiểu dữ liệu, tạo đối tượng hàng hóa tương ứng với loại hàng hóa, lưu vào cơ sở dữ liệu và hiển thị thông báo thành công, sau đó chuyển hướng về trang danh sách hàng hóa
    product_type = request.form.get("product_type")
    name = request.form.get("name")
    code = request.form.get("code")
    unit = request.form.get("unit")

    import_price = request.form.get("import_price")
    sale_price = request.form.get("sale_price")
    stock = request.form.get("stock")
    import_date = request.form.get("import_date")

    import_price = float(import_price)  # chuyển đổi giá trị nhập khẩu sang kiểu float, nếu có lỗi sẽ gán giá trị mặc định là 0
    sale_price = float(sale_price) # chuyển đổi giá trị bán ra sang kiểu float, nếu có lỗi sẽ gán giá trị mặc định là 0
    stock = int(stock) # chuyển đổi giá trị tồn kho sang kiểu int, nếu có lỗi sẽ gán giá trị mặc định là 0
    import_date = datetime.strptime(import_date, "%Y-%m-%d").date() # chuyển đổi giá trị ngày nhập khẩu sang kiểu date, nếu có lỗi sẽ gán giá trị mặc định là ngày hiện tại

    if product_type == "painting":
        brand_name = request.form.get("brand_name")

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
        source = request.form.get("source")

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