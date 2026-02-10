import os
from flask import Flask, render_template, request, redirect, url_for, flash

from extensions import db
from services.customer_service import (
    list_customers, get_customer, create_customer, update_customer, delete_customer
)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "shop.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():# tạo bảng tự động , 
    db.create_all()


@app.route("/")# thêm list và search
def home():
    return redirect(url_for("customers"))


@app.route("/customers")
def customers():
    kw = request.args.get("kw", "").strip()
    customers = list_customers(kw)
    return render_template("customers.html", customers=customers, kw=kw)

@app.route("/customers/add", methods=["GET", "POST"])# thêm thông tin về khách hàng 
def customer_add():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()
        total_spent_raw = request.form.get("total_spent", "0").strip()
        customer_type = request.form.get("customer_type", "regular").strip()

        if not name:
            flash("tên không được để trống", "danger")
            return render_template("customer_form.html", mode="add", customer=None)

        if not phone.isdigit():
            flash("SĐT phải là số", "danger")
            return render_template("customer_form.html", mode="add", customer=None)

        try:
            total_spent = int(total_spent_raw)
            if total_spent < 0:
                total_spent = 0
        except:
            flash("tổng tiền đã mua phải là số", "danger")
            return render_template("customer_form.html", mode="add", customer=None)

        create_customer(name, phone, address, total_spent, customer_type)
        flash("Thêm khách hàng thành công", "success")
        return redirect(url_for("customers"))

    return render_template("customer_form.html", mode="add", customer=None)

@app.route("/customers/<int:cid>/edit", methods=["GET", "POST"]) # phần chỉnh sửa khách hàng 
def customer_edit(cid):
    customer = get_customer(cid)
    if not customer:
        return "Customer not found", 404

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()
        total_spent_raw = request.form.get("total_spent", "0").strip()

        if not name:
            flash("tên không được để trống", "danger")
            return render_template("customer_form.html", mode="edit", customer=customer)

        if not phone.isdigit():
            flash("SĐT phải là số", "danger")
            return render_template("customer_form.html", mode="edit", customer=customer)

        try:
            total_spent = int(total_spent_raw)
            if total_spent < 0:
                total_spent = 0
        except:
            flash("tổng tiền đã mua phải là số", "danger")
            return render_template("customer_form.html", mode="edit", customer=customer)

        update_customer(customer, name, phone, address, total_spent)
        flash("cập nhật khách hàng thành công", "success")
        return redirect(url_for("customers"))

    return render_template("customer_form.html", mode="edit", customer=customer)

@app.route("/customers/<int:cid>/delete", methods=["POST"])# xóa khách hàng khỏi danh sách 
def customer_delete(cid):
    customer = get_customer(cid)
    if not customer:
        return "Customer not found", 404

    delete_customer(customer)
    flash("đã xóa khách hàng", "success")
    return redirect(url_for("customers"))


if __name__ == "__main__":
    app.run(debug=True)
