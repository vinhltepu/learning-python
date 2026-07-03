from pydantic_settings import BaseSettings
# tạo ra class Settings để lưu trữ các cấu hình của ứng dụng, sử dụng pydantic_settings để đọc các giá trị từ biến môi trường hoặc file .env
class Settings(BaseSettings):
    PROJECT_NAME: str = "Quang Thuy Grocery Store API"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./shop.db"

settings = Settings()