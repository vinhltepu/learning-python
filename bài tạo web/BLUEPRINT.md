## 1. Context (Bối cảnh & mục tiêu)

Xây dựng ứng dụng web quản lý cửa hàng tạp hóa ngành mộc gia đình **Quang Thúy** — quản lý hàng hóa, khách hàng và hóa đơn bán hàng, với giao diện web chạy local.

Mục tiêu cụ thể:
- Thay thế sổ sách thủ công bằng web app có database bền vững (SQLite).
- Quản lý 3 module chính: hàng hóa (Product), khách hàng (Customer), hóa đơn (Invoice).
- Áp dụng đầy đủ OOP: inheritance, polymorphism, encapsulation, abstraction.
- Giao diện web rõ ràng, dùng Bootstrap 5 CDN, không cần JavaScript phức tạp.
- Chạy local: `python app.py` → `http://127.0.0.1:5000`.

**Yêu cầu kỹ thuật bắt buộc:**
- Python 3.x + Flask + Flask-SQLAlchemy + Jinja2 templates.
- SQLite tự tạo file `shop.db` qua `db.create_all()`.
- Tối thiểu 6–8 class Python (models), chia module rõ ràng.
- Form validation + flash message xử lý lỗi.

## 2. Kiến trúc tổng thể

┌──────────────────────────────────────────────┐
│            Trình duyệt (localhost:5000)       │
└─────────────────────┬────────────────────────┘
                      │ HTTP request
          ┌───────────▼───────────┐
          │     Flask App         │
          │   (app.py — factory)  │
          └──┬──────┬──────┬──────┘
             │      │      │   Blueprint routing
    ┌────────▼──┐ ┌──▼───┐ ┌──▼──────┐
    │ /goods    │ │/cust-│ │/invoices│
    │ goods_bp  │ │omers │ │invoices_│
    │           │ │_bp   │ │bp       │
    └────────┬──┘ └──┬───┘ └──┬──────┘
             │       │        │   gọi service/model
    ┌────────▼───────▼────────▼──────┐
    │           models/              │
    │  Product   Customer   Invoice  │
    │  Painting  Regular    InvDetail│
    │  Wood      VIP                 │
    └────────────────┬───────────────┘
                     │ SQLAlchemy ORM
          ┌──────────▼──────────┐
          │    SQLite (shop.db)  │
          │  products            │
          │  painting_products   │
          │  wood_products       │
          │  customers           │
          │  regular_customers   │
          │  vip_customers       │
          │  invoices            │
          │  invoice_details     │
          └─────────────────────┘


Lý do chọn:
- Flask Blueprint thay vì 1 file routes duy nhất: tách biệt goods / customers / invoices, dễ debug và mở rộng.
- Factory pattern (`create_app()`): tránh circular import giữa `app.py` và `models/`.
- Joined Table Inheritance của SQLAlchemy: `Product` → `PaintingProduct` / `WoodProduct` lưu ở bảng riêng, truy vấn polymorphic tự động.
- SQLite: đủ cho cửa hàng nhỏ, không cần cài thêm server DB, file `.db` dễ backup.



## 3. Tech stack chi tiết

### Backend
| Layer | Lựa chọn | Dùng ở đâu |

| Web framework | **Flask 2.3** | `app.py` — tạo app, đăng ký blueprint |
| ORM | **Flask-SQLAlchemy 3.1** | `models/` — định nghĩa class → bảng DB |
| Template engine | **Jinja2** (built-in Flask) | `templates/*.html` — render HTML động |
| Form data | **request.form** (Flask built-in) | `routes/*.py` — nhận dữ liệu từ form |
| Flash message | **flash()** (Flask built-in) | `routes/*.py` — thông báo lỗi / thành công |
| Database | **SQLite** (qua SQLAlchemy) | `instance/shop.db` — lưu toàn bộ data |

### Frontend
| Layer | Lựa chọn | Dùng ở đâu |

| CSS framework | **Bootstrap 5** (CDN) | `base.html` — layout, bảng, form, badge |
| Icon | **Bootstrap Icons** (CDN) | `base.html`, navbar, nút thao tác |
| JavaScript | Vanilla JS (tối thiểu) | `invoices_form.html` — thêm/xóa dòng sản phẩm, tính tiền realtime |
| Custom CSS | `static/css/styles.css` | hover card, màu sắc riêng |

### OOP concepts — dùng ở file nào
| Khái niệm | File áp dụng | Cụ thể |

| Inheritance | `models/goods.py` | `PaintingProduct(Product)`, `WoodProduct(Product)` |
| Inheritance | `models/customers.py` | `RegularCustomer(Customer)`, `VIPCustomer(Customer)` |
| Polymorphism | `models/goods.py` | `show_product_info()`, `get_extra_info()` — 3 lớp trả về khác nhau |
| Polymorphism | `models/customers.py` | `get_discount_rate()` — Regular trả 0, VIP trả 5–10% |
| Encapsulation | `models/customers.py` | `@property customer_name`, `@property points` + setter/deleter |
| Abstraction | `models/customers.py` | `get_discount_rate()` ở lớp cha = interface, lớp con tự implement |
| @classmethod | `models/invoices.py` | `Invoice.revenue_by_day()`, `Invoice.revenue_by_month()` |
| db.Model| tất cả `models/` | kế thừa `db.Model` → SQLAlchemy tự tạo bảng |



## 4. Cấu trúc module (file layout)
 
grocery_store/
│
├── app.py                        # Factory create_app(), đăng ký 3 blueprint, route index
├── config.py                     # Class Config: SECRET_KEY, SQLALCHEMY_DATABASE_URI
├── requirements.txt              # Flask, Flask-SQLAlchemy, Werkzeug
│
├── models/                       # Tầng dữ liệu — 8 class Python
│   ├── __init__.py               # export tất cả class để import gọn
│   ├── goods.py                  # Product, PaintingProduct, WoodProduct
│   ├── customers.py              # Customer, RegularCustomer, VIPCustomer
│   └── invoices.py               # Invoice, InvoiceDetail
│
├── routes/                       # Tầng xử lý request — 3 Blueprint
│   ├── __init__.py               # routes_bp (không dùng trực tiếp, chỉ để package)
│   ├── goods.py                  # goods_bp: list, add, edit, delete
│   ├── customers.py              # customers_bp: list, add, edit, delete
│   └── invoices.py               # invoices_bp: list, create, detail, stats
│
├── templates/                    # Jinja2 HTML — 10 file
│   ├── base.html                 # layout chung: navbar, flash, footer
│   ├── index.html                # trang chủ: thống kê nhanh + cảnh báo hết hàng
│   ├── goods.html                # bảng danh sách hàng hóa + tìm kiếm
│   ├── goods_form.html           # form thêm/sửa (toggle field theo loại sản phẩm)
│   ├── customers.html            # bảng danh sách khách hàng + tìm kiếm
│   ├── customers_form.html       # form thêm/sửa khách hàng
│   ├── invoices.html             # bảng hóa đơn + lọc ngày/khách hàng
│   ├── invoices_form.html        # form tạo hóa đơn (thêm nhiều sản phẩm động)
│   ├── invoices_detail.html      # chi tiết 1 hóa đơn
│   └── stats.html                # thống kê doanh thu + top khách + hàng hết
│
└── static/
    └── css/
        └── styles.css            # custom: card hover, footer, responsive




## 5. Chi tiết từng module

### 5.1 models/goods.py — 3 class

**`Product(db.Model)`** — lớp cha
- Thuộc tính: `id`, `type`, `name`, `code`, `unit`, `import_price`, `sale_price`, `stock`, `import_date`
- `__init__`: nhận tham số, `import_date` mặc định `date.today()` nếu không truyền
- `show_product_info()` — polymorphism: lớp con ghi đè hiển thị thông tin riêng
- `get_extra_info()` — polymorphism: trả `""` ở lớp cha, lớp con trả thông tin đặc trưng
- `is_low_stock()` — trả `True` nếu `stock < 10`

**`PaintingProduct(Product)`** — sản phẩm sơn
- Thêm: `brand_name` (tên hãng sơn)
- Ghi đè `show_product_info()` → hiển thị hãng sơn
- Ghi đè `get_extra_info()` → trả `"Hãng sơn: {brand_name}"`

**`WoodProduct(Product)`** — sản phẩm gỗ
- Thêm: `source` (nguồn nhập hàng)
- Ghi đè `show_product_info()` → hiển thị nguồn nhập
- Ghi đè `get_extra_info()` → trả `"Nguồn nhập: {source}"`

---

### 5.2 models/customers.py — 3 class

**`Customer(db.Model)`** — lớp cha
- Thuộc tính: `id`, `type`, `name`, `phone`, `address`, `total_spent`
- `@property customer_name` + `@setter` → validate tên ≥ 2 ký tự (**encapsulation**)
- `@property points` + `@setter` + `@deleter` → đọc/ghi/xóa `total_spent` có kiểm tra (**encapsulation**)
- `@staticmethod is_valid_phone(phone)` → kiểm tra SĐT chỉ gồm số, ≥ 9 ký tự
- `add_spending(money)` → cộng chi tiêu sau mỗi hóa đơn
- `get_discount_rate()` → **abstraction**: lớp cha trả 0, lớp con tự override
- `get_customer_type_label()` → polymorphism: trả nhãn loại khách hàng

**`RegularCustomer(Customer)`**
- `get_discount_rate()` → luôn trả `0` (không giảm giá)

**`VIPCustomer(Customer)`**
- `get_discount_rate()` → trả `0.10` nếu `total_spent ≥ 200tr`, `0.05` nếu ≥ `100tr`, còn lại `0` (**polymorphism**)
- `get_discount_label()` → trả chuỗi `"10%"` / `"Chưa đủ điều kiện"`

---

### 5.3 models/invoices.py — 2 class

**`Invoice(db.Model)`**
- Thuộc tính: `id`, `customer_id`, `created_at`, `subtotal`, `discount_rate`, `total_amount`
- Relationship: `details` → danh sách `InvoiceDetail` (cascade delete)
- `calculate_total()` → tính `subtotal` từ `details`, lấy `discount_rate` từ `customer.get_discount_rate()`, tính `total_amount`
- `@classmethod revenue_by_day()` → GROUP BY ngày, trả list `(ngày, tổng)` (**classmethod**: không cần object cụ thể)
- `@classmethod revenue_by_month()` → GROUP BY tháng

**`InvoiceDetail(db.Model)`**
- Thuộc tính: `id`, `invoice_id`, `product_id`, `quantity`, `unit_price`, `line_total`
- `__init__`: nhận `quantity` và `unit_price`, tự tính `line_total = quantity * unit_price`

---

### 5.4 routes/goods.py — goods_bp

| Route | Method | Chức năng |
|---|---|---|
| `/goods/` | GET | Danh sách, tìm kiếm theo tên/mã |
| `/goods/add` | GET | Hiển thị form thêm mới |
| `/goods/add` | POST | Nhận form, validate, tạo object đúng loại, lưu DB |
| `/goods/edit/<id>` | GET | Hiển thị form điền sẵn dữ liệu cũ |
| `/goods/edit/<id>` | POST | Nhận form, validate, cập nhật DB |
| `/goods/delete/<id>` | POST | Xóa sản phẩm (kiểm tra ràng buộc hóa đơn) |

**Validate trong routes:** kiểm tra tên/code không rỗng, giá/số lượng là số không âm, mã hàng không trùng, trường riêng (`brand_name`, `source`) không rỗng theo loại.

---

### 5.5 routes/customers.py — customers_bp

| Route | Method | Chức năng |
|---|---|---|
| `/customers/` | GET | Danh sách, tìm kiếm tên/SĐT |
| `/customers/add` | GET/POST | Form + xử lý thêm mới, validate SĐT |
| `/customers/edit/<id>` | GET/POST | Form + xử lý sửa |
| `/customers/delete/<id>` | POST | Xóa (kiểm tra hóa đơn liên quan) |

---

### 5.6 routes/invoices.py — invoices_bp

| Route | Method | Chức năng |
|---|---|---|
| `/invoices/` | GET | Danh sách, lọc theo ngày / khách hàng |
| `/invoices/create` | GET | Form chọn khách + thêm nhiều sản phẩm |
| `/invoices/create` | POST | Validate → tạo Invoice + InvoiceDetail → trừ tồn kho → cộng điểm khách → `calculate_total()` |
| `/invoices/detail/<id>` | GET | Xem chi tiết 1 hóa đơn |
| `/invoices/stats` | GET | Thống kê doanh thu ngày/tháng, hàng sắp hết, top khách |

**Logic quan trọng trong `create_invoice`:**
1. Tạo `Invoice`, `db.session.flush()` để có `invoice.id`.
2. Vòng lặp từng `product_id[]` + `quantity[]`: kiểm tra tồn kho → tạo `InvoiceDetail` → trừ `product.stock`.
3. Nếu có lỗi → `rollback()` toàn bộ.
4. `invoice.calculate_total()` → `customer.add_spending(total_amount)` → `commit()`.

---

## 6. Templates (Jinja2) — chi tiết

### 6.1 base.html
- Dùng ở: **tất cả trang** (qua `{% extends "base.html" %}`)
- Cung cấp: Bootstrap 5 CDN, Bootstrap Icons CDN, navbar 5 mục, flash message tự động, footer
- Block để override: `{% block title %}`, `{% block content %}`, `{% block scripts %}`

### 6.2 goods_form.html
- Dùng ở: `/goods/add` (GET) và `/goods/edit/<id>` (GET)
- Điểm đặc biệt: `<select name="product_type">` khi đổi loại → JavaScript `toggleExtraFields()` ẩn/hiện `#field_painting` / `#field_wood`
- Action form tự đổi theo `action` variable: `add` → POST `/goods/add`, `edit` → POST `/goods/edit/<id>`

### 6.3 invoices_form.html
- Dùng ở: `/invoices/create` (GET)
- Điểm đặc biệt: JavaScript thêm/xóa dòng sản phẩm (`addRow()` / `removeRow()`), tính tổng realtime (`updateTotals()`), cập nhật thông tin giảm giá khi đổi khách hàng (`updateDiscount()`)
- Gửi dữ liệu nhiều sản phẩm qua `product_id[]` và `quantity[]` (array form field)

---

## 7. Luồng xử lý chính (flow quan trọng nhất)

### Tạo hóa đơn — end to end

```
User chọn khách hàng + sản phẩm + số lượng
          ↓
POST /invoices/create
          ↓
Validate: khách tồn tại? sản phẩm tồn tại? đủ hàng?
          ↓ (nếu lỗi → flash + redirect)
Invoice(customer_id=...) → db.session.add → flush() → lấy invoice.id
          ↓
Vòng lặp từng sản phẩm:
  InvoiceDetail(invoice_id, product_id, qty, unit_price) → add
  product.stock -= qty
          ↓
invoice.calculate_total()
  ├── subtotal = sum(detail.line_total)
  ├── discount_rate = customer.get_discount_rate()   ← polymorphism!
  └── total_amount = subtotal * (1 - discount_rate)
          ↓
customer.add_spending(total_amount)   ← cộng điểm tích lũy
          ↓
db.session.commit()
          ↓
redirect → /invoices/detail/<id>
```

### OOP nổi bật trong luồng này:
- `customer.get_discount_rate()` — gọi **polymorphism**: nếu VIP → 5–10%, Regular → 0%, không cần if/else ở route
- `invoice.calculate_total()` — **encapsulation**: logic tính tiền nằm trong class, route chỉ gọi 1 dòng
- `customer.add_spending()` — **encapsulation**: validate tiền > 0 bên trong class

---

## 8. Xử lý lỗi & Flash message

| Tình huống | Flash type | Nơi xử lý |

| Mã hàng đã tồn tại | `danger` | `routes/goods.py` — `add_goods()` |
| Giá/số lượng âm hoặc không phải số | `danger` | `routes/goods.py` — `add_goods()`, `edit_goods()` |
| SĐT không hợp lệ | `danger` | `routes/customers.py` — validate qua `Customer.is_valid_phone()` |
| Tên khách hàng < 2 ký tự | `danger` | `routes/customers.py` |
| Sản phẩm không đủ tồn kho | `danger` | `routes/invoices.py` — `create_invoice()` |
| Không chọn sản phẩm nào | `danger` | `routes/invoices.py` |
| Xóa sản phẩm đang có trong hóa đơn | `danger` | `routes/goods.py` — `delete_goods()` (catch Exception) |
| Thêm/sửa/xóa thành công | `success` | mọi route sau khi `commit()` |

Flash message hiển thị tự động ở `base.html` qua `get_flashed_messages(with_categories=true)`.


## 9. Verification (cách test end-to-end)

1. **Smoke**: `python app.py` → truy cập `http://127.0.0.1:5000` → trang chủ hiện 3 thẻ thống kê.
2. **Goods**: thêm 1 sản phẩm thường, 1 sản phẩm sơn (điền brand_name), 1 sản phẩm gỗ (điền source) → kiểm tra bảng danh sách hiển thị đúng loại. Tìm kiếm theo tên/mã.
3. **Customers**: thêm khách thường và khách VIP với `total_spent = 150,000,000` → xem cột "Giảm giá" hiển thị đúng `5%`.
4. **Invoice**: tạo hóa đơn cho khách VIP 150tr, thêm 2 sản phẩm → kiểm tra: giảm giá 5% được áp dụng, tồn kho sản phẩm trừ đúng, điểm khách tăng.
5. **Tồn kho**: tạo hóa đơn mua nhiều hơn số hàng có → xem flash `danger` "không đủ hàng".
5. **Stats**: vào `/invoices/stats` → kiểm tra doanh thu ngày, top khách, hàng sắp hết.
7. **Error handling**: thêm hàng với mã trùng → flash lỗi. SĐT chứa chữ → flash lỗi.
5