from pydantic import BaseSettings
# Đây là file cấu hình chính của ứng dụng, sử dụng Pydantic để quản lý các biến môi trường và cấu hình ứng dụng một cách dễ dàng và hiệu quả.
class Settings(BaseSettings):
    PROJECT_NAME: str = "Book Management API"

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./app.db"
    
settings = Settings()

