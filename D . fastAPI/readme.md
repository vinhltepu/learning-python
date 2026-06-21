# Xây dựng một Book Management API hoàn chỉnh bằng FastAPI gồm 3 đối tượng chính 

- Author sử dụng thuộc tính name và bio , một tác giả sẽ có nhiều sách 
- Category sử dụng thuộc tính name , một sách sẽ có nhiều danh mục 
- Book sử dụng title, description , published_year, author_id , category_id ,cover_image , creaed_at, updated_at  

# Các API sẽ xây dựng 
- GET /authors — Lấy danh sách tác giả
- POST /authors — Tạo tác giả mới → trả về 201
- GET /authors/{id} — Xem chi tiết 1 tác giả
- PUT /authors/{id} — Cập nhật → trả về 200
- DELETE /authors/{id} — Xóa → trả về 204 (không có body) 

# Fast API là gì 
FastAPI là framework Python chuyên dùng để xây dựng API. Ưu điểm nổi bật:
-  Code ngắn, dễ đọc
- Tự sinh tài liệu — chạy lên là có ngay /docs (Swagger UI) và /redoc để test, không cần Postman
- Validate dữ liệu tự động — nhờ Pydantic
- Hiệu năng cao — hỗ trợ bất đồng bộ (async) nhờ Starlette

# Lý do tại sao cần API 
Tách biệt Frontend & Backend rõ ràng:
- Backend chỉ lo trả về data dạng JSON. Frontend muốn hiển thị như thế nào là việc của nó. Hai team làm việc độc lập nhau

Tái sử dụng cho nhiều client
Một backend duy nhất có thể phục vụ cả web lẫn mobile — cả hai chỉ cần gọi cùng một API, không cần viết lại logic

# Mục đích của 3 file authors, books, categories trong api/endpoints
Đây là pattern "Router Separation" (tách router theo resource) trong FastAPI. Cả 3 file có cấu trúc giống nhau vì chúng đều là API Router độc lập, mỗi file quản lý một nhóm tài nguyên riêng biệt.

# cấu trúc tổng thể 
FAST-API-BOOKS/
├── api/
├── core/
│   ├── __init__.py
│   └── config.py        → Cấu hình chung của ứng dụng (tên app, database URI)
├── db/
│   ├── __init__.py
│   ├── base.py          → Khai báo Base model cho SQLAlchemy
│   └── session.py       → Khởi tạo engine và SessionLocal kết nối database
├── models/
│   ├── __init__.py
│   ├── author.py        → Model SQLAlchemy của Tác giả (ánh xạ bảng DB)
│   ├── book.py          → Model SQLAlchemy của Sách (ánh xạ bảng DB)
│   └── category.py      → Model SQLAlchemy của Thể loại (ánh xạ bảng DB)
├── schemas/
│   ├── __init__.py
│   ├── author.py        → Pydantic schema validate dữ liệu Tác giả
│   ├── book.py          → Pydantic schema validate dữ liệu Sách
│   └── category.py      → Pydantic schema validate dữ liệu Thể loại
├── static/
│   └── covers/          → Thư mục lưu ảnh bìa sách
└── main.py              → Điểm khởi chạy ứng dụng FastAPI