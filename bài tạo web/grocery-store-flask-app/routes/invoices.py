from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.invoices import Invoice, InvoiceDetail
from models.customers import Customer
from models.goods import Product
from datetime import datetime

invoices_bp = Blueprint('invoices', __name__)

@invoices_bp.route("/invoices")
def list_invoices():
    """
    Hiển thị danh sách hóa đơn.
    Có thể lọc hóa đơn theo khách hàng.
    """
    # Lấy ID khách hàng từ query string để lọc
    customer_id_search = request.args.get("customer_id", "")
    
    # Bắt đầu với một truy vấn cơ bản cho tất cả hóa đơn
    query = Invoice.query
    
    # Nếu có ID khách hàng, lọc danh sách hóa đơn theo ID đó
    if customer_id_search:
        query = query.filter(Invoice.customer_id == customer_id_search)
        
    # Sắp xếp các hóa đơn theo ngày tạo mới nhất và lấy tất cả
    invoices = query.order_by(Invoice.created_at.desc()).all()
    
    # Lấy danh sách tất cả khách hàng để hiển thị trong bộ lọc
    customers = Customer.query.all()
    
    # Render template, truyền dữ liệu hóa đơn và khách hàng
    return render_template(
        "invoices.html", 
        invoices=invoices, 
        customers=customers, 
        customer_id_search=customer_id_search
    )

@invoices_bp.route("/invoices/add", methods=["GET", "POST"])
def add_invoice():
    """
    Xử lý việc thêm hóa đơn mới (cả GET và POST).
    """
    # Nếu là request POST, xử lý dữ liệu từ form
    if request.method == "POST":
        customer_id = request.form.get("customer_id")
        product_ids = request.form.getlist("product_id[]")
        quantities = request.form.getlist("quantity[]")

        # Kiểm tra xem khách hàng đã được chọn chưa
        if not customer_id:
            flash("Vui lòng chọn một khách hàng.", "danger")
            return redirect(url_for("invoices.add_invoice"))

        customer = Customer.query.get(customer_id)
        if not customer:
            flash("Khách hàng không tồn tại.", "danger")
            return redirect(url_for("invoices.add_invoice"))

        # Tạo một đối tượng hóa đơn mới
        new_invoice = Invoice(customer_id=customer.id, created_at=datetime.now())
        db.session.add(new_invoice)
        
        subtotal = 0
        
        # Lặp qua các sản phẩm được thêm vào hóa đơn
        for i in range(len(product_ids)):
            product_id = product_ids[i]
            quantity = int(quantities[i]) if quantities[i].isdigit() else 0

            # Bỏ qua nếu không có sản phẩm hoặc số lượng là 0
            if not product_id or quantity <= 0:
                continue

            product = Product.query.get(product_id)
            if not product or product.stock < quantity:
                flash(f"Không đủ hàng cho sản phẩm '{product.name}'.", "warning")
                continue

            # Trừ số lượng tồn kho
            product.stock -= quantity
            
            # Tính tổng tiền cho dòng sản phẩm này
            line_total = product.sale_price * quantity
            subtotal += line_total
            
            # Tạo chi tiết hóa đơn
            detail = InvoiceDetail(
                product_id=product.id,
                quantity=quantity,
                unit_price=product.sale_price,
                line_total=line_total
            )
            new_invoice.details.append(detail)

        # Nếu không có sản phẩm nào hợp lệ, hủy thao tác
        if not new_invoice.details:
            flash("Hóa đơn phải có ít nhất một sản phẩm hợp lệ.", "danger")
            db.session.rollback()
            return redirect(url_for("invoices.add_invoice"))

        # Tính toán tổng tiền cuối cùng
        new_invoice.calculate_total()
        
        # Cập nhật điểm tích lũy cho khách hàng
        customer.total_spent += new_invoice.total_amount

        # Lưu các thay đổi vào database
        db.session.commit()

        flash("Tạo hóa đơn thành công!", "success")
        return redirect(url_for("invoices.list_invoices"))

    # Nếu là request GET, chỉ hiển thị form
    customers = Customer.query.all()
    products = Product.query.all()
    return render_template("add_invoice.html", customers=customers, products=products)


