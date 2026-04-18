from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.customers import Customer, RegularCustomer, VIPCustomer

Customers_bp = Blueprint('customers', __name__) 

@Customers_bp.route("/customers") # định nghĩa route để hiển thị danh sách khách hàng
def list_customers():
    keyword = request.args.get("keyword", "") # lấy từ khóa tìm kiếm từ tham số truy vấn 
    keyword = keyword.strip() # loại bỏ khoảng trắng ở đầu và cuối từ khóa

    if keyword != "":# nếu có từ khóa, thực hiện truy vấn tìm kiếm khách hàng theo tên hoặc số điện thoại
        customers = Customer.query.filter(# tìm kiếm khách hàng theo tên hoặc số điện thoại chứa từ khóa
            (Customer.name.contains(keyword)) |
            (Customer.phone.contains(keyword))
        ).all()
    else:
        customers = Customer.query.all()# nếu không có từ khóa, lấy tất cả khách hàng

    return render_template(
        "customers.html",# hiển thị danh sách khách hàng và từ khóa tìm kiếm trên trang customers.html
        customers=customers,# truyền danh sách khách hàng vào template để hiển thịn
        keyword=keyword # truyền từ khóa tìm kiếm vào template để hiển thị trong ô tìm kiếm
    )
    
    
@Customers_bp.route("/customers/add", methods=["POST"]) # định nghĩa route để thêm khách hàng mới, chỉ chấp nhận phương thức POST
def add_customer():
    customer_type = request.form.get("customer_type")
    name = request.form.get("name")
    phone = request.form.get("phone")
    address = request.form.get("address")
    total_spent = request.form.get("total_spent")

    if total_spent == "": # nếu trường tổng chi tiêu để trống, gán giá trị mặc định là 0
        total_spent = 0# nếu trường tổng chi tiêu không phải là số hợp lệ, gán giá trị mặc định là 0
    else:
        total_spent = float(total_spent)# chuyển đổi giá trị tổng chi tiêu sang kiểu float, nếu có lỗi sẽ gán giá trị mặc định là 0
        if total_spent < 0: # nếu tổng chi tiêu là số âm, gán giá trị mặc định là 0
            total_spent = 0# kiểm tra tính hợp lệ của số điện thoại, nếu không hợp lệ sẽ hiển thị thông báo lỗi và chuyển hướng về trang danh sách khách hàng

    if Customer.is_valid_phone(phone) == False: # kiểm tra tính hợp lệ của số điện thoại, nếu không hợp lệ sẽ hiển thị thông báo lỗi và chuyển hướng về trang danh sách khách hàng
        flash("Số điện thoại không hợp lệ", "danger")
        return redirect(url_for("customers.list_customers"))

    if customer_type == "vip": # nếu loại khách hàng là VIP, tạo đối tượng VIPCustomer, ngược lại tạo đối tượng RegularCustomer và lưu vào cơ sở dữ liệu
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