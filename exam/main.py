import os

from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError

from extensions import db
from db import create_tables
from services.product_service import ProductService

app = Flask(__name__)

# flash message cần SECRET_KEY
app.config["SECRET_KEY"] = "dev"

# SQLite tự tạo shop.db trong cùng thư mục exam/
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "shop.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# tạo bảng tự động
with app.app_context():
    create_tables()

services = ProductService()


@app.route("/")
def home():
    return redirect(url_for("products"))


# danh sách + tìm kiếm theo tên hoặc mã
@app.route("/products")
def products():
    q = (request.args.get("q") or "").strip()
    items = services.get_all(q=q if q else None)
    return render_template("products.html", items=items, q=q)


# thêm sản phẩm
@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        # validate cơ bản
        name = (request.form.get("name") or "").strip()
        code = (request.form.get("code") or "").strip()
        unit = (request.form.get("unit") or "").strip()
        imported_date = (request.form.get("imported_date") or "").strip()

        if not name or not code or not unit or not imported_date:
            flash("Vui lòng nhập đủ: Tên, Mã, Đơn vị, Ngày nhập.", "danger")
            return render_template("product_form.html", mode="add", product=None, form=request.form)

        try:
            product = services.create_from_form(request.form)
            services.add(product)
            flash("Thêm hàng hóa thành công!", "success")
            return redirect(url_for("products"))
        except ValueError:
            db.session.rollback()
            flash("Giá/Số lượng không hợp lệ.", "danger")
        except IntegrityError:
            db.session.rollback()
            flash("Mã hàng hóa đã tồn tại (bị trùng).", "danger")

        return render_template("product_form.html", mode="add", product=None, form=request.form)

    return render_template("product_form.html", mode="add", product=None, form={})


# sửa sản phẩm
@app.route("/products/<int:pid>/edit", methods=["GET", "POST"])
def edit_product(pid):
    product = services.get(pid)
    if not product:
        return "Product not found", 404

    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        code = (request.form.get("code") or "").strip()
        unit = (request.form.get("unit") or "").strip()
        imported_date = (request.form.get("imported_date") or "").strip()

        if not name or not code or not unit or not imported_date:
            flash("Vui lòng nhập đủ: Tên, Mã, Đơn vị, Ngày nhập.", "danger")
            return render_template("product_form.html", mode="edit", product=product, form=request.form)

        try:
            services.update_from_form(product, request.form)
            flash("Cập nhật hàng hóa thành công!", "success")
            return redirect(url_for("products"))
        except ValueError:
            db.session.rollback()
            flash("Giá/Số lượng không hợp lệ.", "danger")
        except IntegrityError:
            db.session.rollback()
            flash("Mã hàng hóa bị trùng.", "danger")

        return render_template("product_form.html", mode="edit", product=product, form=request.form)

    return render_template("product_form.html", mode="edit", product=product, form={})


# xóa sản phẩm
@app.route("/products/<int:pid>/delete", methods=["POST"])
def delete_product(pid):
    product = services.get(pid)
    if not product:
        return "Product not found", 404

    services.delete(product)
    flash("Đã xóa hàng hóa.", "success")
    return redirect(url_for("products"))

@app.route("/invoices")
def invoices():
    rows = invoice_services.get_all()
    return render_template("invoices.html", invoices=rows)


@app.route("/invoices/new", methods=["GET", "POST"])
def new_invoice():
    # lấy danh sách customer + products để render form
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone, total_spent, customer_type FROM customers ORDER BY id DESC")
    customers = cur.fetchall()

    cur.execute("SELECT id, name, code, sell_price, stock FROM products ORDER BY id DESC")
    products = cur.fetchall()
    conn.close()

    if request.method == "POST":
        try:
            customer_id = int(request.form.get("customer_id"))
        except:
            customer_id = 0
        cart = {}
        for p in products:
            pid = p["id"] if "id" in p.keys() else p[0]
            qty_raw = request.form.get(f"qty_{pid}", "0")
            try:
                qty = int(qty_raw)
            except:
                qty = 0
            if qty > 0:
                cart[pid] = qty

        try:
            invoice_id = invoice_services.create_invoice(customer_id, cart)
            flash(f"Tạo hóa đơn thành công! Mã hóa đơn: {invoice_id}", "success")
            return redirect(url_for("invoice_detail", invoice_id=invoice_id))
        except ValueError as e:
            flash(str(e), "danger")

    return render_template("invoice_form.html", customers=customers, products=products)


@app.route("/invoices/<int:invoice_id>")
def invoice_detail(invoice_id):
    invoice, items = invoice_services.get_detail(invoice_id)
    if not invoice:
        return "Invoice not found", 404
    return render_template("invoice_detail.html", invoice=invoice, items=items)
if __name__ == "__main__":
    app.run(debug=True)
