from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models.customers import Customer, RegularCustomer, VIPCustomer

customers_bp = Blueprint('customers', __name__)

@customers_bp.route("/")
def list_customers():
    keyword = request.args.get("keyword", "").strip()

    if keyword:
        customers = Customer.query.filter(
            (Customer.name.contains(keyword)) |
            (Customer.phone.contains(keyword))
        ).all()
    else:
        customers = Customer.query.all()

    return render_template(
        "customers.html",
        customers=customers,
        keyword=keyword
    )


@customers_bp.route("/add", methods=["POST"])
def add_customer():
    customer_type = request.form.get("customer_type")
    name = request.form.get("name")
    phone = request.form.get("phone")
    address = request.form.get("address")
    total_spent = request.form.get("total_spent")

    if total_spent == "":
        total_spent = 0
    else:
        try:
            total_spent = float(total_spent)
        except ValueError:
            total_spent = 0
        if total_spent < 0:
            total_spent = 0

    if not Customer.is_valid_phone(phone):
        flash("Số điện thoại không hợp lệ", "danger")
        return redirect(url_for("customers.list_customers"))

    if customer_type == "vip":
        customer = VIPCustomer(
            name=name,
            phone=phone,
            address=address,
            total_spent=total_spent
        )
    else:
        customer = RegularCustomer(
            name=name,
            phone=phone,
            address=address,
            total_spent=total_spent
        )

    db.session.add(customer)
    db.session.commit()

    flash("Thêm khách hàng thành công", "success")
    return redirect(url_for("customers.list_customers"))


@customers_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_customer(id):
    customer = Customer.query.get_or_404(id)

    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        address = request.form.get("address")
        total_spent = request.form.get("total_spent")

        if total_spent == "":
            total_spent = 0
        else:
            try:
                total_spent = float(total_spent)
            except ValueError:
                total_spent = 0

        customer.name = name
        customer.phone = phone
        customer.address = address
        customer.total_spent = total_spent

        db.session.commit()
        flash("Cập nhật khách hàng thành công", "success")
        return redirect(url_for("customers.list_customers"))

    return render_template("edit_customer.html", customer=customer)


@customers_bp.route("/delete/<int:id>", methods=["POST"])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)

    db.session.delete(customer)
    db.session.commit()

    flash("Xóa khách hàng thành công", "success")
    return redirect(url_for("customers.list_customers"))

