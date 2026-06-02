from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.invoices import Invoice, InvoiceDetail
from models.customers import Customer
from models.goods import Product

invoices_bp = Blueprint('invoices', __name__)

@invoices_bp.route("/")
def list_invoices():
    customer_id = request.args.get("customer_id", type=int)
    created_at = request.args.get("created_at", type=str)

    query = Invoice.query.order_by(Invoice.created_at.desc())
    if customer_id:
        query = query.filter_by(customer_id=customer_id)

    if created_at:
        try:
            date_value = datetime.strptime(created_at, "%Y-%m-%d").date()
            query = query.filter(db.func.date(Invoice.created_at) == date_value)
        except ValueError:
            flash("Ngày lọc không hợp lệ. Vui lòng dùng định dạng YYYY-MM-DD.", "warning")

    invoices = query.all()
    customers = Customer.query.order_by(Customer.name).all()
    return render_template(
        "invoices.html",
        invoices=invoices,
        customers=customers,
        selected_customer=customer_id,
        selected_date=created_at,
    )


@invoices_bp.route("/create", methods=["GET", "POST"])
def create_invoice():
    customers = Customer.query.order_by(Customer.name).all()
    products = Product.query.order_by(Product.name).all()

    if request.method == "POST":
        customer_id = request.form.get("customer_id", type=int)
        product_ids = request.form.getlist("product_id")
        quantities = request.form.getlist("quantity")

        if not customer_id:
            flash("Vui lòng chọn khách hàng.", "danger")
            return redirect(url_for("invoices.create_invoice"))

        customer = Customer.query.get(customer_id)
        if not customer:
            flash("Khách hàng không tồn tại.", "danger")
            return redirect(url_for("invoices.create_invoice"))

        invoice = Invoice(customer_id=customer.id, created_at=datetime.now())

        for index in range(len(product_ids)):
            try:
                product_id = int(product_ids[index])
            except (ValueError, TypeError):
                continue

            quantity_text = quantities[index]
            if not quantity_text or not quantity_text.isdigit():
                continue

            quantity = int(quantity_text)
            if quantity <= 0:
                continue

            product = Product.query.get(product_id)
            if not product:
                continue

            if product.stock < quantity:
                flash(f"Sản phẩm {product.name} không đủ hàng.", "warning")
                continue

            product.stock -= quantity
            detail = InvoiceDetail(
                product_id=product.id,
                quantity=quantity,
                unit_price=product.sale_price
            )
            invoice.details.append(detail)

        if not invoice.details:
            flash("Hóa đơn phải có ít nhất một sản phẩm.", "danger")
            return redirect(url_for("invoices.create_invoice"))

        invoice.calculate_total()
        customer.add_spending(invoice.total_amount)
        db.session.add(invoice)
        db.session.commit()

        flash("Tạo hóa đơn thành công.", "success")
        return redirect(url_for("invoices.list_invoices"))

    return render_template(
        "create_invoice.html",
        customers=customers,
        products=products,
    )


@invoices_bp.route("/<int:invoice_id>")
def invoice_detail(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    return render_template("invoice_detail.html", invoice=invoice)


@invoices_bp.route("/<int:invoice_id>/delete", methods=["POST"])
def delete_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)

    for detail in invoice.details:
        if detail.product:
            detail.product.stock += detail.quantity

    db.session.delete(invoice)
    db.session.commit()

    flash("Xóa hóa đơn thành công.", "success")
    return redirect(url_for("invoices.list_invoices"))
