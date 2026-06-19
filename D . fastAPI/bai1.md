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

