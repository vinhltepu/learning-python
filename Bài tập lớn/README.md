# ĐỀ BÀI BÀI TẬP LỚN
## Xây dựng ứng dụng web quản lý cửa hàng tạp hóa Quang Thúy

### Mục tiêu
Xây dựng một ứng dụng web đơn giản quản lý hàng hóa, khách hàng và hóa đơn bán hàng cho cửa hàng bán tạp hóa ngành mộc gia đình Quang Thúy. Ứng dụng phải sử dụng đầy đủ các khái niệm OOP trong Python, kết hợp với framework Flask để tạo giao diện web, và lưu trữ dữ liệu bền vững vào database SQLite. Ưu tiên sử dụng tiếng Anh trong code. 

### Công nghệ bắt buộc
- Python 3.x
- Flask (web framework)
- Flask-SQLAlchemy (để làm việc với database SQLite)
- Jinja2 templates (HTML + CSS cơ bản, không cần JavaScript phức tạp)
- SQLite làm database (file .db tự động tạo)

### Yêu cầu chức năng chính (phải có giao diện web cho tất cả)
1. **Quản lý hàng hóa (Product)**
   - Danh sách hàng hóa (hiển thị bảng).
   - Thêm, sửa, xóa hàng hóa (qua form HTML).
   - Tìm kiếm theo tên hoặc mã.
   - Thuộc tính: id (tự tăng), tên, mã hàng hóa, đơn vị (kg, cái, hộp...), giá nhập, giá bán, số lượng tồn kho, ngày nhập.
   - Áp dụng inheritance: lớp cha `Product`, ít nhất 2 lớp con (ví dụ: `PaintingProduct` có thêm Tên hãng sơn; `WoodProduct` có thêm nguồn nhập hàng).

2. **Quản lý khách hàng (Customer)**
   - Danh sách khách hàng.
   - Thêm, sửa, xóa, tìm kiếm.
   - Thuộc tính: id (tự tăng), tên, số điện thoại, địa chỉ, điểm tích lũy (tổng tiền đã mua).
   - Inheritance: lớp `RegularCustomer` kế thừa `Customer`, lớp `VIPCustomer`có phương thức tính giảm giá dựa trên điểm tích lũy (ví dụ tổng tiền đã mua trên 100 triệu thì giảm giá 5%, trên 200 triệu thì giảm giá 10%).

3. **Quản lý hóa đơn bán hàng (Invoice)**
   - Tạo hóa đơn mới: chọn khách hàng, thêm nhiều sản phẩm vào giỏ (có thể dùng form với multiple items), tính tổng tiền, áp dụng giảm giá nếu có, cập nhật tồn kho.
   - Danh sách hóa đơn (theo ngày hoặc khách hàng).
   - Xem chi tiết hóa đơn.

4. **Chức năng phụ**
   - Thống kê: sản phẩm sắp hết (<10), doanh thu theo ngày/tháng, top khách hàng mua nhiều.
   - Trang chủ có menu rõ ràng (navbar).
   - Xử lý lỗi cơ bản (flash message): không đủ hàng, nhập sai dữ liệu...

### Yêu cầu về OOP và thiết kế code
- Ít nhất 6-8 class (Product và subclasses, Customer và subclasses, Invoice, InvoiceDetail...).
- Áp dụng đầy đủ: inheritance, polymorphism (ví dụ phương thức tính giá khác nhau), encapsulation (private attributes + property), abstraction.
- Sử dụng Flask-SQLAlchemy để định nghĩa models (class kế thừa db.Model).
- Code chia module rõ ràng: models.py, routes.py (hoặc phân theo blueprint nếu nâng cao), templates/, static/.

### Yêu cầu kỹ thuật khác
- Database: dùng SQLite (tạo file shop.db tự động qua db.create_all()).
- Giao diện: HTML đơn giản, dùng Bootstrap (CDN) để đẹp hơn (không bắt buộc nhưng khuyến khích).
- Bảo mật cơ bản: không cần login phức tạp, nhưng xử lý form validation.
- Chạy local: python app.py → truy cập http://127.0.0.1:5000
- Chạy đúng đầy đủ chức năng 
- Code sạch, comment, cấu trúc module hợp lý
- Báo cáo và README
- Chỉ được dùng AI để giải thích các khái niệm, không được dùng AI để code thay, cậu biết chỗ nào AI nó code chỗ nào cháu code đấy!

### Giao nộp
- Toàn bộ source code trên GitHub (public repo).
- File README.md: hướng dẫn cài đặt, cách chạy, chụp hình các trang chính.
- Báo cáo ngắn (3-5 trang): 
  - Mô tả cấu trúc project.
  - Giải thích các khái niệm OOP đã áp dụng.
  - Khó khăn gặp phải và cách giải quyết.