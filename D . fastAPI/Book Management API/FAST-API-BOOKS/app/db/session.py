from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL, # Tạo một engine kết nối đến cơ sở dữ liệu SQLite dựa trên đường dẫn được định nghĩa trong settings.SQLALCHEMY_DATABASE_URL
    connect_args={"check_same_thread": False} if settings.SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {} # Nếu đường dẫn cơ sở dữ liệu bắt đầu bằng "sqlite", thêm đối số connect_args để cho phép nhiều luồng truy cập vào cùng một kết nối SQLite. Nếu không phải là SQLite, không cần thêm đối số này.
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
# Tạo một sessionmaker để quản lý các phiên làm việc với cơ sở dữ liệu. Các đối số autocommit và autoflush được đặt thành False để kiểm soát việc commit và flush thủ công. Đối số bind được sử dụng để liên kết session với engine đã tạo ở trên.