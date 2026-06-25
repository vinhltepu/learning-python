from typing import Generator

from app.db.session import SessionLocal
#Đây là một dependency function được FastAPI inject vào các route thông qua Depends(get_db)
# mở sesion get_db sau đó trả cho route handler sử dụng, khi route xử lý xong thì đóng sesion lại
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()   

# Luồng hoạt động:

# db = SessionLocal() : Mở 1 kết nối đến database
# yield db : Trả kết nối đó cho route handler sử dụng, tạm dừng hàm tại đây
# Khi route xử lý xong : hàm tiếp tục chạy xuống finally
# db.close()  : Đóng kết nối lại dù thành công hay có lỗi
