# Toán tử và Biểu thức
## hầu hết các câu lệnh (dòng logic) bạn viết sẽ chứa các biểu thức
## một ví dụ đơn giản của biểu thức là 2 + 3
## một biểu thức có thể được phân tích thành toán tử và toán hạng
## toán tử là các chức năng thực hiện một việc gì đó
## toán tử có thể được biểu diễn bằng các ký hiệu như + hoặc bằng các từ khóa đặc biệt
## toán tử yêu cầu một số dữ liệu để hoạt động và dữ liệu đó được gọi là toán hạng
## trong biểu thức 2 + 3 thì 2 và 3 là các toán hạng

# Người vận hành 
## toán hạng là dữ liệu mà toán tử hoạt động lên 
## toán tử + thêm hai đối tượng lại với nhau 
## toán tử - trừ một số khỏi số khác, và có thể biểu diễn số âm 
## toán tử * trả về tích hai số hoặc lặp chuỗi tương ứng số lần 
## toán tử ** trả về x mũ y 
## toán tử / chia x cho y 
## toán tử // chia và làm tròn xuống 
## toán tử % trả về phần dư của phép chia 
## toán tử << dịch bit của số sang trái n
## toán tử >> dịch bit của số sang phải n
## toán tử & là phép AND bitwise 
## toán tử | là phép OR bitwise 
## toán tử ^ là phép XOR bitwise 
## toán tử ~ là phép đảo bit 
## các toán tử so sánh (<, >, <=, >=, ==, !=) trả về True hoặc False 
## phép not là phủ định logic 
## toán tử and và or là phép AND và OR logic 
## có thể dùng các toán tử rút gọn để thực hiện phép tính rồi gán kết quả vào biến (ví dụ a *= 3 thay vì a = a * 3) 
## python có quy tắc ưu tiên toán tử xác định thứ tự đánh giá biểu thức 
## ưu tiên toán tử quyết định trước hay sau khi thực hiện từng phép trong biểu thức 
## để thay đổi thứ tự đánh giá có thể dùng ngoặc để nhóm biểu thức 
## toán tử cùng mức ưu tiên được đánh giá từ trái sang phải 
## ví dụ biểu thức tính diện tích và chu vi dùng toán tử và biểu thức 
## các toán tử, toán hạng và biểu thức là các khối xây dựng cơ bản của chương trình python

# Phím tắt cho phép tính và gán toán học
## toán tử rút gọn khi gán
## có thể kết hợp phép toán và phép gán trong một câu lệnh
## ví dụ a = a * 3 có thể viết thành a *= 3
## dạng của nó là  var = var phép_toán biểu_thức → var phép_toán= biểu_thức

## thứ tự đánh giá 
## python sử dụng độ ưu tiên của toán tử để xác định thứ tự tính toán
## lambdaBiểu thức Lambda
## if - else: Biểu thức điều kiện
## or: Boolean HOẶC
## and: Boolean AND
## not x: Boolean NOT
## in, not in, is, is not, <, <=, >, >=, !=, ==: So sánh, bao gồm kiểm tra tư cách thành viên và kiểm tra danh tính.
## |: Phép toán OR bitwise
## ^: Phép XOR bitwise
## &: Phép AND bitwise
## <<, >>Ca làm việc
## +, -Phép cộng và phép trừ
## *, /, //, %Phép nhân, phép chia, phép chia lấy phần nguyên và phép chia lấy phần dư
## +x, -x, ~x: Dương, Âm, phép toán NOT bitwise
## **Lũy thừa
## x[index], x[index:index], x(arguments...), x.attribute: Đăng ký, cắt lát, gọi hàm, tham chiếu thuộc tính
## (expressions...), [expressions...], {key: value...}, {expressions...}: Hiển thị liên kết hoặc bộ dữ liệu, hiển thị danh sách, hiển thị từ điển, hiển thị tập hợp
## các toán tứ cùng độ ưu tiên thì được tính theo từ trái sang phải 
