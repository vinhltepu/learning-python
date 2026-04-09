# luồng điều khiển 
## muốn thay đổi luồng điểu khiển trong python ta có 3 câu lệnh là if , for while 
 
# câu lệnh if 
## Câu lệnh if được sử dụng để kiểm tra một điều kiện
##  nếu điều kiện đúng, ta sẽ thực thi một khối lệnh (gọi là khối if ), ngược lại, ta sẽ xử lý một khối lệnh khác (gọi là khối else )
## Mệnh đề else là tùy chọn
## chương trình nhận một giá trị đoán từ người dùng để so sánh với một số đã cho
## số cần đoán được gán trước cho biến number, ví dụ là 23
## chương trình sử dụng hàm input để hiển thị thông báo và chờ người dùng nhập dữ liệu
## giá trị người dùng nhập vào từ input là một chuỗi
## chuỗi này được chuyển thành số nguyên bằng hàm int
## giá trị sau khi chuyển được lưu vào biến guess
## chương trình so sánh giá trị guess với number bằng câu lệnh if
## nếu guess bằng number thì in ra thông báo đoán đúng
## nếu guess nhỏ hơn number thì chương trình thông báo cần đoán số lớn hơn
## nếu guess lớn hơn number thì chương trình thông báo cần đoán số nhỏ hơn
## các điều kiện được liên kết bằng cấu trúc if elif else
## cấu trúc này giúp chương trình gọn hơn và giảm mức thụt lề
## mỗi câu lệnh if elif else đều kết thúc bằng dấu hai chấm
## các câu lệnh bên trong khối phải được thụt lề nhất quán
## python dựa vào thụt lề để xác định câu lệnh nào thuộc cùng một khối
## thụt lề sai sẽ làm chương trình báo lỗi
## có thể đặt một câu lệnh if bên trong một if khác
## cấu trúc này được gọi là if lồng nhau
## elif và else là các phần tùy chọn trong câu lệnh if
## một câu lệnh if hợp lệ tối thiểu chỉ cần if và một điều kiện đúng
## sau khi thực thi xong if elif else python tiếp tục chạy câu lệnh tiếp theo
## khi chương trình chạy hết các câu lệnh thì chương trình kết thúc
## python không có câu lệnh switch như c hoặc c++
## if elif else thường được dùng để thay thế switch trong python

# câu lệnh while 
## câu lệnh while dùng để lặp lại một khối lệnh chừng nào điều kiện còn đúng
## while là một câu lệnh lặp
## điều kiện của while được kiểm tra trước mỗi lần lặp
## nếu điều kiện là true thì khối while được thực thi
## nếu điều kiện là false thì vòng lặp kết thúc
## vòng lặp while có thể có mệnh đề else (tùy chọn)
## khối else của while được thực thi khi điều kiện trở thành false
## khối else không được thực thi nếu vòng lặp bị thoát bằng break
## các câu lệnh trong while phải được thụt lề đúng
## biến điều kiện thường được khởi tạo trước vòng lặp
## giá trị biến điều kiện có thể thay đổi bên trong vòng lặp để dừng lặp
## true và false là kiểu dữ liệu Boolean
## true tương đương 1 và false tương đương 0
## while thường dùng khi không biết trước số lần lặp
## khác với c/c+= python thì cho phép dùng else với while

# vòng lặp for 
## vòng lặp for..in là một câu lệnh lặp
## for..in dùng để lặp qua một chuỗi các đối tượng
## chuỗi là một tập hợp các mục được sắp xếp theo thứ tự
## vòng lặp for duyệt qua từng mục trong chuỗi
## hàm range() được dùng để tạo ra một dãy số
## range(a, b) tạo dãy số bắt đầu từ a đến trước b
## mặc định range() có bước nhảy là 1
## có thể truyền tham số thứ ba cho range() để chỉ định bước nhảy
## range() chỉ tạo từng giá trị một khi cần
## dùng list(range()) nếu muốn lấy toàn bộ dãy số
## for i in range(1,5) tương đương với lặp qua [1, 2, 3, 4]
## mỗi lần lặp một giá trị trong chuỗi được gán cho biến lặp
## khối lệnh trong for được thực thi cho mỗi giá trị
## mệnh đề else của for là tùy chọn
## else được thực thi sau khi vòng lặp kết thúc
## else không được thực thi nếu gặp câu lệnh break
## vòng lặp for trong Python khác với for trong C/C++
## for trong Python tương tự foreach trong C#
## for trong Python đơn giản và ít lỗi hơn so với C/C++

# câu lệnh break 
## câu lệnh break dùng để thoát khỏi vòng lặp
## break dừng vòng lặp ngay lập tức dù điều kiện chưa sai
## break dùng được trong cả vòng lặp while và for
## khi gặp break vòng lặp sẽ kết thúc ngay
## nếu vòng lặp bị thoát bằng break thì khối else của vòng lặp không được thực thi
## trong ví dụ vòng lặp chạy vô hạn với while True
## chương trình liên tục nhận dữ liệu người dùng bằng input()
## khi người dùng nhập 'quit' thì điều kiện đúng và break được thực thi
## sau break chương trình thoát khỏi vòng lặp
## lệnh len() dùng để lấy độ dài của chuỗi nhập vào
## sau khi thoát vòng lặp chương trình tiếp tục chạy câu lệnh phía sau
## câu lệnh print('Done') luôn được thực thi sau khi vòng lặp kết thúc
 
# câu lệnh continue 
## câu lệnh continue dùng để bỏ qua phần còn lại của vòng lặp hiện tại
## continue không thoát vòng lặp mà chuyển sang lần lặp tiếp theo
## continue dùng được trong cả vòng lặp while và for
## khi gặp continue các câu lệnh phía sau trong vòng lặp không được thực thi
## vòng lặp trong ví dụ chạy liên tục với while True
## chương trình nhận dữ liệu người dùng bằng input()
## nếu người dùng nhập 'quit' thì vòng lặp kết thúc bằng break
## hàm len() được dùng để kiểm tra độ dài chuỗi nhập vào
## sau continue chương trình quay lại đầu vòng lặp
## nếu độ dài chuỗi đủ lớn thì các câu lệnh còn lại trong vòng lặp được thực thi
## continue giúp bỏ qua dữ liệu không hợp lệ và tiếp tục xử lý các dữ liệu khác