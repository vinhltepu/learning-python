import os
from flask import Flask, render_template, request, redirect, url_for, flash
from extensions import db

# import models để db.create_all() tạo đủ bảng
import models  # noqa

from services.product_service import ProductService
from services.customer_service import CustomerService
from services.invoice_service import InvoiceService

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "shop.db")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path.replace("\\", "/")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# tự tạo DB và bảng
with app.app_context():
    db.create_all()

product_services = ProductService()
customer_services = CustomerService()
invoice_services = InvoiceService()

@app.route("/")
def home():
    return redirect(url_for("products"))

# ================== PRODUCT ==================
@app.route("/products")
def products():
    q = (request.args.get("q") or "").strip()
    items = product_services.get_all(q=q if q else None)
    return render_template("products.html", items=items, q=q)

@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        try:
            p = product_services.create_from_form(request.form)
            product_services.add(p)
            flash("Thêm hàng hóa thành công!", "success")
            return redirect(url_for("products"))
        except Exception as e:
            flash(str(e), "danger")
            return render_template("product_form.html", mode="add", product=None, form=request.form)

    return render_template("product_form.html", mode="add", product=None, form={})

@app.route("/products/<int:pid>/edit", methods=["GET", "POST"])
def edit_product(pid):
    product = product_services.get(pid)
    if not product:
        return "Product not found", 404

    if request.method == "POST":
        try:
            product_services.update_from_form(product, request.form)
            flash("Cập nhật hàng hóa thành công!", "success")
            return redirect(url_for("products"))
        except Exception as e:
            flash(str(e), "danger")
            return render_template("product_form.html", mode="edit", product=product, form=request.form)

    return render_template("product_form.html", mode="edit", product=product, form={})

@app.route("/products/<int:pid>/delete", methods=["POST"])
def delete_product(pid):
    product = product_services.get(pid)
    if not product:
        return "Product not found", 404
    product_services.delete(product)
    flash("Đã xóa hàng hóa.", "success")
    return redirect(url_for("products"))

# ================== CUSTOMER ==================
@app.route("/customers")
def customers():
    q = (request.args.get("q") or "").strip()
    items = customer_services.get_all(q=q if q else None)
    return render_template("customers.html", items=items, q=q)

@app.route("/customers/add", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        try:
            c = customer_services.create_from_form(request.form)
            customer_services.add(c)
            flash("Thêm khách hàng thành công!", "success")
            return redirect(url_for("customers"))
        except Exception as e:
            flash(str(e), "danger")
            return render_template("customer_form.html", mode="add", customer=None, form=request.form)

    return render_template("customer_form.html", mode="add", customer=None, form={})

@app.route("/customers/<int:cid>/edit", methods=["GET", "POST"])
def edit_customer(cid):
    customer = customer_services.get(cid)
    if not customer:
        return "Customer not found", 404

    if request.method == "POST":
        try:
            customer_services.update_from_form(customer, request.form)
            flash("Cập nhật khách hàng thành công!", "success")
            return redirect(url_for("customers"))
        except Exception as e:
            flash(str(e), "danger")
            return render_template("customer_form.html", mode="edit", customer=customer, form=request.form)

    return render_template("customer_form.html", mode="edit", customer=customer, form={})

@app.route("/customers/<int:cid>/delete", methods=["POST"])
def delete_customer(cid):
    customer = customer_services.get(cid)
    if not customer:
        return "Customer not found", 404
    customer_services.delete(customer)
    flash("Đã xóa khách hàng.", "success")
    return redirect(url_for("customers"))

# ================== INVOICE ==================
@app.route("/invoices")
def invoices():
    customer_id_raw = (request.args.get("customer_id") or "").strip()
    date_from = (request.args.get("date_from") or "").strip()
    date_to = (request.args.get("date_to") or "").strip()

    customer_id = int(customer_id_raw) if customer_id_raw.isdigit() else None

    rows = invoice_services.get_all(
        customer_id=customer_id,
        date_from=date_from or None,
        date_to=date_to or None
    )
    customers_list = customer_services.get_all()

    return render_template(
        "invoices.html",
        invoices=rows,
        customers=customers_list,
        customer_id=customer_id,
        date_from=date_from,
        date_to=date_to
    )

@app.route("/invoices/new", methods=["GET", "POST"])
def new_invoice():
    customers_list = customer_services.get_all()
    products_list = product_services.get_all()

    if request.method == "POST":
        try:
            customer_id = int(request.form.get("customer_id") or 0)

            cart = {}
            for p in products_list:
                qty_raw = request.form.get(f"qty_{p.id}", "0")
                try:
                    qty = int(qty_raw)
                except:
                    qty = 0
                if qty > 0:
                    cart[p.id] = qty

            invoice_id = invoice_services.create_invoice(customer_id, cart)
            flash(f"Tạo hóa đơn thành công! Mã hóa đơn: {invoice_id}", "success")
            return redirect(url_for("invoice_detail", invoice_id=invoice_id))
        except Exception as e:
            flash(str(e), "danger")

    return render_template("invoice_form.html", customers=customers_list, products=products_list)

@app.route("/invoices/<int:invoice_id>")
def invoice_detail(invoice_id):
    invoice, items = invoice_services.get_detail(invoice_id)
    if not invoice:
        return "Invoice not found", 404
    return render_template("invoice_detail.html", invoice=invoice, items=items)

if __name__ == "__main__":
    app.run(debug=True)