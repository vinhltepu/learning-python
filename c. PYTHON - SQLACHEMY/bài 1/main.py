from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker 
from sqlalchemy import Column, Integer, String, Float


url = 'sqlite:///example.db'  # URL kết nối đến cơ sở dữ liệu SQLite

engine = create_engine(url)  # Tạo engine kết nối đến cơ sở dữ liệu SQLite



# Ví dụ URL kết nối PostgreSQL (chỉ để tham khảo):
# postgresql+psycopg2://username:password@host:port/database_name

# dialect: loại cơ sở dữ liệu (ví dụ: sqlite, mysql, postgresql, mssql).
# driver: driver để kết nối (ví dụ: pymysql, psycopg2, pyodbc).
# username, password, host, port, database_name: Thông tin kết nối thực tế của cơ sở dữ liệu của bạn.

Base = declarative_base()  # Tạo lớp cơ sở cho các mô hình của bạn

Base.metadata.create_all(engine)  # Tạo tất cả các bảng trong cơ sở dữ liệu dựa trên các mô hình đã định nghĩa


# tạo bảng 

# -products
# - id: int (primary key) 
# - name: string
# - price: float
# - description: string


class Product(Base):
    __tablename__ = 'products'  # Tên bảng trong cơ sở dữ liệu

    id = Column(Integer, primary_key=True)  # Cột id là khóa chính
    name = Column(String)  # Cột name kiểu string
    price = Column(Float)  # Cột price kiểu float
    description = Column(String)  # Cột description kiểu string
 