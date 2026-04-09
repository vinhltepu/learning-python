## input and output
sẽ có những tình huống mà chương trình của bạn cần tương tác với người dùng
bạn có thể nhận đầu vào từ người dùng và sau đó in ra kết quả
có thể sử dụng hàm input để nhận dữ liệu
có thể sử dụng hàm print để xuất dữ liệu
có thể sử dụng các phương thức của lớp str để xuất dữ liệu
phương thức rjust dùng để căn phải chuỗi với chiều rộng được chỉ định
xử lý tập tin là một dạng nhập xuất dữ liệu phổ biến
khả năng tạo đọc và ghi tập tin là rất cần thiết đối với nhiều chương trình

# Input from user
sử dụng cắt lát để đảo ngược văn bản
có thể tạo lát cắt chuỗi bằng cú pháp seq[a:b]
có thể dùng đối số bước để điều khiển chiều cắt lát
bước âm như -1 sẽ đảo ngược chuỗi
hàm input nhận một chuỗi làm lời nhắc và hiển thị cho người dùng
input chờ người dùng nhập dữ liệu và nhấn enter
input trả về chuỗi mà người dùng đã nhập
so sánh chuỗi gốc và chuỗi đảo ngược để kiểm tra palindrome
nếu hai chuỗi bằng nhau thì đó là văn bản đối xứng

# Homework exercise
Bài tập yêu cầu cải thiện chương trình kiểm tra văn bản đối xứng bằng cách bỏ qua dấu câu, khoảng trắng và phân biệt chữ hoa chữ thường để nhận diện đúng các trường hợp như “Rise to vote, sir.”
# Files
mở và sử dụng các tệp để đọc hoặc ghi bằng cách tạo một đối tượng của file và sử dụng các phương thức read, readline hoặc write
khả năng đọc hoặc ghi vào tệp phụ thuộc vào chế độ bạn đã chỉ định cho việc mở tệp
khi bạn đã sử dụng xong tệp, bạn gọi phương thức close để thông báo cho python
chế độ có thể là đọc ('r'), ghi ('w') hoặc nối thêm ('a')
theo mặc định, open() mở tệp ở chế độ đọc văn bản
ghi dữ liệu vào tệp bằng phương thức write và đọc từng dòng bằng readline
khi readline trả về chuỗi rỗng nghĩa là đã đến cuối tệp
chương trình đã ghi và đọc dữ liệu từ tệp poem.txt
# Pickle
python cung cấp mô-đun chuẩn pickle dùng để lưu trữ và lấy lại các đối tượng python từ tệp
việc lưu trữ đối tượng vào tệp được gọi là lưu trữ bền vững
để ghi dữ liệu, tệp phải được mở ở chế độ ghi nhị phân 'wb'
sử dụng hàm pickle.dump để lưu đối tượng vào tệp
sau khi lưu có thể xóa đối tượng trong chương trình
để đọc lại dữ liệu, mở tệp ở chế độ đọc nhị phân 'rb'
sử dụng hàm pickle.load để lấy đối tượng từ tệp
quá trình lưu gọi là pickling và quá trình đọc lại gọi là unpickling
# Unicode
unicode cho phép biểu diễn cả ký tự tiếng anh và không phải tiếng anh
python 3 mặc định lưu trữ chuỗi dưới dạng unicode
python 2 cần dùng kiểu dữ liệu unicode với tiền tố u để xử lý ngôn ngữ không phải tiếng anh
khi truyền dữ liệu qua internet cần chuyển unicode thành byte
quy tắc chuyển đổi unicode sang byte gọi là mã hóa
utf-8 là một kiểu mã hóa phổ biến
có thể đọc ghi dữ liệu utf-8 bằng cách dùng tham số encoding trong hàm open
chỉ sử dụng encoding khi mở tệp ở chế độ văn bản
khi dùng chuỗi unicode cần khai báo encoding utf-8 ở đầu chương trình
