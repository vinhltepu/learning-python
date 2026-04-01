# ORM
ORM (Object-Relational Mapping) là một kỹ thuật giúp thao tác với cơ sở dữ liệu dễ dàng hơn bằng cách ánh xạ các   bảng trong database thành các đối tượng trong code. Thay vì viết SQL thủ công, ta dùng các phương thức của ORM để truy vấn, thêm, sửa, xóa dữ liệu.

Tên SQLAlchemy là sự kết hợp giữa SQL (Structured Query Language) và Alchemy (thuật giả kim, một ngành khoa học có liên quan đến việc chuyển đổi kim loại bình thường thành vàng và tìm kiếm "chìa khóa" của sự sống bất tử).

Trong bối cảnh của thư viện này, tên SQLAlchemy mang ý nghĩa là một công cụ mạnh mẽ để "chuyển đổi" và làm việc với
số dữ liệu (giống như cách thuật giả kim tìm cách chuyển hóa vật chất). Thư viện này giúp lập trình viên "chuyển đổi" các đối tượng trong mã nguồn thành các câu lệnh SQL, đồng thời tối giản và tối ưu hóa quá trình tương tác với cơ sở dữ liệu.

Với SQLAlchemy, bạn có thể dễ dàng biến các đối tượng trong Python thành các bảng cơ sở dữ liệu và thực hiện các thao tác CRUD (Create, Read, Update, Delete) mà không cần phải viết SQL thủ công. Tóm lại, SQLAlchemy giúp bạn "hóa vàng" công việc tương tác với cơ sở dữ liệu, làm cho nó dễ dàng và hiệu quả hơn.

SQLAlchemy là một thư viện mạnh mẽ của Python giúp bạn tương tác với "cơ sở dữ liệu quan hệ" bằng cách sử dụng mô hình lập trình hướng đối tượng (OOP). Nó cung cấp hai cách để làm việc với cơ sở dữ liệu: SQLAlchemy ORM và SQLAlchemy Core.


Các Chuỗi Kết Nối (Connection Strings) Phổ Biến:
SQLite: 'sqlite:///path_to_database.db' hoặc 'sqlite:///:memory:' cho cơ sở dữ liệu trong bộ nhớ
MySQL: 'mysql+pymysql://username:password@localhost:3306/mydatabase'
PostgreSQL: 'postgresql://username:password@localhost:5432/mydatabase'
SQL Server: 'mssql+pyodbc://username:password@localhost:1433/mydatabase?driver=SQL+Server'
Oracle: 'oracle+cx_oracle://username:password@localhost:1521/?sid=service_name'


Số lượng dấu / quyết định kiểu kết nối:
sqlite://: Kết nối đến cơ sở dữ liệu trong bộ nhớ (in-memory).
sqlite:///: Kết nối tới cơ sở dữ liệu lưu trong tệp với đường dẫn tương đối.
sqlite:////: Kết nối tới cơ sở dữ liệu lưu trong tệp với đường dẫn tuyệt đối.


Hàm declarative_base() trả về một class cơ sở (base class). Các lớp (model) của bạn sẽ kế thừa
class này.

Class cơ sở này giúp SQLAlchemy hiểu rằng các lớp con của nó là những mô hình cần ánh xạ với các
bảng trong cơ sở dữ liệu.
Các lớp (models) bạn định nghĩa sẽ là các bảng trong cơ sở dữ liệu.

Mỗi lớp con của Base sẽ được SQLAlchemy coi là một bảng cơ sở dữ liệu.
Các thuộc tính (attributes) của lớp sẽ trở thành các cột trong bảng.
Quản lý Metadata:

Base cũng quản lý thông tin về cơ sở dữ liệu như metadata, tức là thông tin mô tả về các bảng,
các cột và các kiểu dữ liệu.