from flask import Flask, render_template, request, redirect, url_for
from db import create_tables
from services.product_service import ProductService
from models.product import Product, PaintingProduct, WoodProduct

app = Flask(__name__)
create_tables()
services = ProductService()

@app.route("/")
def home():
    return redirect(url_for("products"))

@app.route("/products")
def products():
    items = services.get_all()
    return render_template("products.html", items=items)  # items là list Product objects

@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        # Lấy data từ form
        data = {k: request.form.get(k, "").strip() for k in ["name", "code", "unit", "imported_date"]}
        data["import_price"] = float(request.form.get("import_price", 0))
        data["sell_price"] = float(request.form.get("sell_price", 0))
        data["stock"] = int(request.form.get("stock", 0))

        # Tạo object (có thể thêm logic chọn loại PaintingProduct nếu form có field paint_brand)
        product = Product(**data)  # hoặc check if 'paint_brand' in request.form → PaintingProduct

        services.add(product)
        return redirect(url_for("products"))
    return render_template("product_form.html", mode="add", product=None)

# Tương tự cho edit/delete: update/delete