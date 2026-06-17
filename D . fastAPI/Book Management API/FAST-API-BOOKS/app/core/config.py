from pydantic import BaseModel

class Settings(BaseModel): 
    PROJECT_NAME: str = "FAST-API-BOOKS" # Tên dự án, được định nghĩa dưới dạng một chuỗi. Đây là tên của ứng dụng hoặc API mà bạn đang xây dựng.

    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./books.db" # Đường dẫn đến cơ sở dữ liệu SQLite, được định nghĩa dưới dạng một chuỗi. Cấu trúc của chuỗi này cho biết rằng chúng ta đang sử dụng SQLite và cơ sở dữ liệu sẽ được lưu trữ trong tệp "books.db" nằm trong thư mục hiện tại (./).

settings = Settings() # Tạo một instance của lớp Settings, cho phép bạn truy cập các thuộc tính đã định nghĩa trong lớp này thông qua biến settings. Ví dụ, bạn có thể truy cập tên dự án bằng cách sử dụng settings.PROJECT_NAME hoặc đường dẫn cơ sở dữ liệu bằng cách sử dụng settings.SQLALCHEMY_DATABASE_URL.
