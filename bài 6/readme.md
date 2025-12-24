## mô dun
# mô đun 
mô-đun dùng để tái sử dụng nhiều hàm trong các chương trình khác nhau
cách đơn giản nhất là tạo một tệp có phần mở rộng .py chứa các hàm và biến
mô-đun có thể được viết bằng python hoặc bằng ngôn ngữ gốc như c
một mô-đun có thể được nhập bởi chương trình khác để sử dụng chức năng của nó
đây là cách sử dụng thư viện chuẩn của python
sử dụng câu lệnh import để nhập mô-đun
mô-đun sys chứa các chức năng liên quan đến trình thông dịch python và hệ thống
khi python thực thi import sys nó sẽ tìm mô-đun sys
nếu mô-đun không phải tích hợp sẵn python sẽ tìm trong các thư mục nằm trong sys.path
quá trình khởi tạo mô-đun chỉ được thực hiện lần đầu tiên khi import
các biến trong mô-đun được truy cập bằng dấu chấm ví dụ sys.argv
sys.argv là danh sách các đối số dòng lệnh được truyền cho chương trình
tên tập lệnh đang chạy luôn là phần tử đầu tiên trong sys.argv
python bắt đầu đếm chỉ số từ 0
sys.path chứa danh sách các thư mục nơi các mô-đun được nhập
chuỗi rỗng trong sys.path cho biết thư mục hiện tại cũng được dùng để tìm mô-đun
thư mục hiện tại là thư mục mà từ đó chương trình được khởi chạy

# các tệp .pyc được biên dịch byte
việc nhập một mô-đun tương đối tốn kém vì vậy python sử dụng một số thủ thuật để làm cho quá trình này nhanh hơn
một cách là tạo các tệp được biên dịch byte với phần mở rộng .pyc
đây là dạng trung gian mà python chuyển đổi chương trình thành
tệp .pyc rất hữu ích khi bạn nhập mô-đun lần sau từ một chương trình khác vì nó sẽ nhanh hơn nhiều
các tệp được biên dịch byte này không phụ thuộc vào nền tảng
các tệp .pyc thường được tạo trong cùng thư mục với các tệp .py tương ứng
nếu python không có quyền ghi vào các tệp trong thư mục đó thì các tệp .pyc sẽ không được tạo
 

# câu lệnh from..import
nếu bạn muốn nhập trực tiếp biến argv vào chương trình của mình thì bạn có thể sử dụng câu lệnh from sys import argv
nói chung hãy tránh sử dụng câu lệnh from..import
hãy sử dụng câu lệnh import thay vào đó
điều này là vì chương trình của bạn sẽ tránh được xung đột tên và sẽ dễ đọc hơn

# một mô đun name 
mỗi module đều có một tên và các câu lệnh trong module có thể biết được tên đó
name giúp xác định module đang chạy độc lập hay được nhập từ module khác
khi một module được nhập lần đầu mã bên trong nó sẽ được thực thi
có thể dùng name để làm cho module hoạt động khác nhau tùy theo cách sử dụng
mỗi mô-đun python đều có nam
nếu name là 'main' thì module đang được chạy độc lập

# tự tạo một mô đun 
mọi chương trình python đều là một module chỉ cần có phần mở rộng .py
module có thể được dùng lại trong các chương trình python khác
module cần nằm cùng thư mục với chương trình import hoặc trong các thư mục của sys.path
có thể truy cập các thành viên của module bằng ký hiệu dấu chấm
cú pháp from import cũng cho kết quả giống import thông thường
có thể xảy ra xung đột tên khi dùng from import nếu trùng tên như version
nên ưu tiên dùng import module để tránh xung đột dù code dài hơn
from module import * sẽ không import các tên bắt đầu bằng hai dấu gạch dưới
nên tránh sử dụng import sao vì không rõ ràng
python đề cao nguyên tắc rõ ràng hơn là ngầm định

# hàm dir chức năng 
hàm dir() trả về danh sách các tên được định nghĩa trong một đối tượng
nếu đối tượng là mô-đun thì dir() cho biết các hàm lớp và biến trong mô-đun đó
khi truyền tên mô-đun vào dir() hàm sẽ trả về danh sách tên của mô-đun đ
khi không truyền đối số dir() sẽ trả về danh sách tên của mô-đun hiện tại
các mô-đun đã import cũng xuất hiện trong kết quả của dir()
khi tạo thêm biến mới thì tên biến sẽ xuất hiện trong danh sách dir()
khi xóa biến bằng del thì tên biến sẽ biến mất khỏi kết quả dir()
lệnh del dùng để xóa biến và sau đó không thể truy cập biến đó nữa
dir() có thể dùng cho mọi đối tượng ví dụ như lớp str
hàm vars() cũng cho biết thuộc tính và giá trị nhưng không dùng được trong mọi trường hợp

# gói hàng 
các gói dùng để tổ chức các mô-đun khi chương trình trở nên lớn hơn
biến thường nằm trong hàm hàm và biến toàn cục nằm trong module
gói là các thư mục chứa các mô-đun python
mỗi gói cần có tệp init.py để python nhận biết đó là một gói
gói có thể chứa các gói con và các mô-đun bên trong
các gói giúp tổ chức mô-đun theo cấu trúc phân cấp rõ ràng
cấu trúc gói thường được sử dụng nhiều trong thư viện chuẩn python