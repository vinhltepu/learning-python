## problem solving
# the problem 
vấn đề :tôi cần một chương trình tạo bản sao lưu tất cả các tập tin quan trọng của mình
thông tin hiện có chưa đủ để chúng ta bắt đầu giải quyết
cần phân tích thêm để xác định những tập tin cần sao lưu cách lưu trữ và vị trí lưu trữ
sau khi phân tích vấn đề một cách kỹ lưỡng chúng ta thiết kế chương trình
các tệp và thư mục cần sao lưu được chỉ định trong một danh sách
bản sao lưu phải được lưu trữ trong thư mục sao lưu chính
các tệp được sao lưu vào một tệp zip
tên của tệp lưu trữ zip là ngày và giờ hiện tại
sử dụng lệnh zip tiêu chuẩn trên gnu/linux hoặc unix
người dùng windows có thể cài đặt lệnh zip từ dự án gnuwin32 và thêm vào biến môi trường hệ thống

# The Solution
vì thiết kế chương trình đã ổn định chúng ta có thể viết mã để triển khai giải pháp
chương trình được lưu dưới dạng backup_ver1.py
các tệp và thư mục cần sao lưu được chỉ định trong danh sách source
thư mục sao lưu chính được chỉ định bằng biến target_dir
các tệp được sao lưu vào một tệp zip
tên tệp zip là ngày và giờ hiện tại được tạo bằng time.strftime
thư mục sao lưu sẽ được tạo nếu chưa tồn tại
lệnh zip được sử dụng để nén các tệp và thư mục cần sao lưu
chương trình chạy lệnh zip bằng os.system
nếu lệnh zip chạy thành công chương trình thông báo sao lưu thành công
nếu chương trình không hoạt động cần kiểm tra lệnh zip trong terminal hoặc cmd
chương trình sử dụng mô đun os và time
os.sep được dùng để đảm bảo chương trình chạy trên nhiều hệ điều hành
tùy chọn -r của lệnh zip cho phép nén đệ quy các thư mục
chương trình đang ở giai đoạn kiểm thử để kiểm tra và gỡ lỗi
sau khi chương trình hoạt động đúng có thể sử dụng trong giai đoạn vận hành
nếu chương trình không hoạt động đúng cần quay lại thiết kế hoặc gỡ lỗi

# Second Version
phiên bản đầu tiên của kịch bản phần mềm hoạt động tốt nhưng có thể tinh chỉnh để hiệu quả hơn trong sử dụng hàng ngày
đây được gọi là giai đoạn bảo trì phần mềm
cải tiến là cơ chế đặt tên tập tin tốt hơn
sử dụng ngày hiện tại làm tên thư mục con trong thư mục sao lưu chính
sử dụng thời gian làm tên tập tin zip
các bản sao lưu được lưu trữ theo cấu trúc phân cấp nên dễ quản lý hơn
tên tập tin ngắn gọn hơn
các thư mục riêng biệt giúp kiểm tra đã sao lưu dữ liệu cho mỗi ngày hay chưa
chương trình được lưu dưới dạng backup_ver2.py
hầu hết chương trình vẫn giữ nguyên so với phiên bản trước
chương trình kiểm tra xem thư mục theo ngày hiện tại có tồn tại hay không
nếu thư mục chưa tồn tại thì tạo mới bằng os.mkdir
tệp zip được tạo trong thư mục theo ngày hiện tại
chương trình sử dụng os.path.exists để kiểm tra sự tồn tại của thư mục

# Third Version
phiên bản thứ hai hoạt động tốt khi thực hiện nhiều bản sao lưu nhưng khó phân biệt mục đích của từng bản sao lưu
cần liên kết các thay đổi với tên của tệp lưu trữ zip
có thể thêm ghi chú do người dùng cung cấp vào tên tệp zip
chương trình này được lưu dưới dạng backup_ver3.py
chương trình được cảnh báo là không hoạt động
python báo lỗi cú pháp syntaxerror invalid syntax
lỗi xảy ra tại dòng tạo biến target
một dòng logic đã bị tách thành hai dòng vật lý
python gặp toán tử cộng nhưng không có toán hạng tiếp theo
python không biết cách tiếp tục thực thi
cần chỉ rõ dòng lệnh tiếp tục bằng dấu gạch chéo ngược
việc sửa lỗi chương trình được gọi là sửa lỗi bug fixing

# Fourth Version
chương trình được lưu dưới dạng backup_ver4.py
chương trình hiện đã hoạt động
chương trình tiếp nhận nhận xét của người dùng bằng hàm input
chương trình kiểm tra người dùng có nhập nhận xét hay không bằng hàm len
nếu người dùng không nhập gì chương trình tạo file zip như trước
nếu người dùng nhập nhận xét nhận xét sẽ được thêm vào tên tệp zip
nhận xét được thêm trước phần mở rộng zip
các khoảng trắng trong nhận xét được thay thế bằng dấu gạch dưới
việc thay thế khoảng trắng giúp quản lý tên tệp dễ dàng hơn
chương trình tạo thư mục theo ngày nếu chưa tồn tại
tệp zip được tạo trong thư mục theo ngày hiện tại

# More Refinements
phiên bản thứ tư hoạt động khá tốt đối với hầu hết người dùng nhưng vẫn có thể cải thiện
có thể thêm mức độ chi tiết cho lệnh zip bằng tùy chọn -v hoặc -q
có thể cho phép truyền thêm các tệp và thư mục qua dòng lệnh
có thể lấy các tệp và thư mục từ danh sách sys.argv
có thể thêm các tệp và thư mục đó vào danh sách source bằng phương thức extend
cải tiến quan trọng nhất là không sử dụng os.system để tạo tệp lưu trữ
có thể sử dụng các mô đun tích hợp sẵn như zipfile hoặc tarfile
các mô đun này thuộc thư viện chuẩn và không phụ thuộc vào chương trình zip bên ngoài
việc sử dụng os.system trong ví dụ chỉ nhằm mục đích sư phạm
có thể thử viết phiên bản thứ năm sử dụng mô đun zipfile thay vì os.system

# The Software Development Process
 đã trải qua các giai đoạn khác nhau trong quá trình viết phần mềm
các giai đoạn có thể được tóm tắt là cái gì phân tích
cách thức thiết kế
thực hiện triển khai
kiểm thử kiểm thử và gỡ lỗi
sử dụng vận hành hoặc triển khai
duy trì cải tiến
phương pháp được khuyến nghị là phân tích và thiết kế trước khi triển khai
bắt đầu với một phiên bản đơn giản
kiểm tra và gỡ lỗi chương trình
sử dụng chương trình để đảm bảo hoạt động đúng như mong đợi
tiếp tục thêm tính năng và lặp lại chu trình thực hiện kiểm tra sử dụng
phần mềm được phát triển chứ không phải được xây dựng