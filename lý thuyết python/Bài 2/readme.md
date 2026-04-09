# installation
## trong cuốn sách này python 3 được hiểu là bất kỳ phiên bản python nào từ 3.6.0 trở lên
## python được tải từ trang https://www.python.org/downloads/ và quá trình cài đặt tương tự như các phần mềm khác trên windows
## đối với các phiên bản windows trước vista chỉ nên sử dụng python 3.4 vì các phiên bản mới hơn yêu cầu windows mới
## khi cài đặt trên windows cần chắc chắn đã chọn add python to path
## có thể chọn customize installation nếu muốn thay đổi vị trí cài đặt python
## python launcher có thể được cài đặt hoặc không và không ảnh hưởng nhiều đến người mới họ
## nếu chưa chọn add python to path khi cài đặt thì cần thêm đường dẫn python vào biến môi trường path
## biến môi trường path cho phép chạy python từ dòng lệnh windows
## để chạy python trên windows mở command prompt và gõ lệnh python
## trên mac os x cài python 3 bằng homebrew với lệnh brew install python3
## trên gnu linux cài python 3 bằng trình quản lý gói của bản phân ph 
## sau khi cài đặt có thể kiểm tra bằng lệnh python3
## có thể xem phiên bản python bằng lệnh $ python3 -v
## từ đây sách giả định rằng python đã được cài đặt và sẵn sàng sử dụng 

# fist stept
## bây giờ chúng ta sẽ học cách chạy chương trình hello world bằng python
## ví dụ này giúp học cách viết lưu và chạy chương trình python
## có hai cách để chạy chương trình python là dùng dấu nhắc trình thông dịch hoặc dùng tệp mã nguồn
## đầu tiên là sử dụng dấu nhắc trình thông dịch
## mở cửa sổ dòng lệnh terminal trên hệ điều hành của bạn
## gõ lệnh python3 và nhấn enter để mở trình thông dịch python
## sau khi khởi động python sẽ thấy dấu nhắc >>>
## dấu nhắc >>> là nơi để bắt đầu gõ các lệnh python
## tại dấu nhắc này nhập lệnh print("Hello World") và nhấn enter
## python sẽ in ra dòng chữ hello world ngay lập tức
## python thực thi lệnh và hiển thị kết quả ngay sau khi nhập
## print là câu lệnh dùng để in giá trị ra màn hình
## để thoát khỏi trình thông dịch trên gnu linux và mac os x nhấn ctrl + d hoặc gõ exit() rồi nhấn enter
## để thoát khỏi trình thông dịch trên windows nhấn enter sau đó nhấn ctrl + z rồi nhấn enter
## không thể gõ lại chương trình tại dấu nhắc mỗi lần muốn chạy nên cần lưu chương trình vào tệp
## để tạo tệp mã nguồn python cần sử dụng một trình soạn thảo văn bản
## một trình soạn thảo tốt giúp viết chương trình python dễ dàng hơn
## trình soạn thảo nên có tính năng tô sáng cú pháp
## người mới bắt đầu được khuyên sử dụng pycharm educational edition
## trên windows không nên dùng notepad vì không hỗ trợ tô sáng cú pháp và thụt lề
## pycharm có sẵn cho windows mac os x và gnu linux
## để viết chương trình bằng tệp mã nguồn tạo tệp hello.py
## chương trình hello world trong tệp chỉ gồm dòng print("hello world")
## tệp python cần được lưu với phần mở rộng là .py
## nên lưu chương trình python trong một thư mục dễ nhớ
## để chạy chương trình mở cửa sổ dòng lệnh và chuyển đến thư mục chứa tệp
## chạy chương trình bằng lệnh python hello.py
## nếu màn hình in ra hello world thì chương trình đã chạy thành công
## python phân biệt chữ hoa chữ thường nên cần gõ đúng cú pháp
## không được có khoảng trắng hoặc tab thừa ở đầu dòng
## một chương trình python được tạo thành từ các câu lệnh
## chương trình đầu tiên chỉ gồm một câu lệnh gọi print
## có thể dùng hàm help để xem trợ giúp cho các hàm hoặc câu lệnh trong python
## có thể thoát khỏi phần trợ giúp bằng cách nhấn phím q
## sau chương này người học đã có thể viết lưu và chạy chương trình python
## các phần tiếp theo sẽ giới thiệu thêm các khái niệm cơ bản của python

# basics
## ta có thể  nhận đầu vào , xử lý kết quả và nhận được kết quả bằng cách sử dụng hằng số và biến 
## biểu tượng #, dùng để ghi chú 
## hằng số là các giá trị cố định như số hoặc chuỗi
## hằng số không thay đổi giá trị trong quá trình chạy
## số trong python có số nguyên và số thực 
## E là kí hiệu của lũy thừa 10 
## chuỗi là 1 dãy kí tự 
## là tập hợp của các từ 
## có thể chỉ định chuỗi bằng dấu ngoặc đơn '' tất cả khoảng trắng trong dấu ngoặc đơn đều được giữ nguyên 
## dấu ngoặc kép " " hoạt động giống dãy ngoặc đơn 
## có thể sử dụng dấu ngoặc đơn và dấu ngoặc kép hai lần một cách tự do bên trong dấu ngoặc kép ba lần
## khi tạo ra 1 chuỗi , không thể thay đổi nó nữa 
## một chuỗi có thể chứa các ký hiệu định dạng và sau đó gọi phương thức format để thay thế chúng bằng các đối số tương ứng
## trong chuỗi, các ký hiệu như {0}, {1} đại diện cho vị trí của các đối số truyền vào format
## {0} tương ứng với đối số đầu tiên, {1} tương ứng với đối số thứ hai vì python đếm từ 0
## phương thức format giúp tạo chuỗi rõ ràng hơn so với việc nối chuỗi thủ công
## khi dùng format, python tự động chuyển các giá trị sang chuỗi nên tránh được lỗi
## có thể bỏ số thứ tự trong dấu {} nếu thứ tự các đối số không bị nhầm lẫn
## ngoài ra, có thể đặt tên cho các tham số trong chuỗi để dễ đọc hơn
## python 3.6 giới thiệu f-string, cho phép chèn trực tiếp biến vào chuỗi bằng cú pháp gọn hơn
## f-string hoạt động bằng cách thay thế giá trị của biến vào đúng vị trí trong chuỗi
## phương thức format còn cho phép định dạng chi tiết như số chữ số thập phân hoặc căn lề văn bản
## hàm print mặc định thêm ký tự xuống dòng ở cuối mỗi lần in
## có thể dùng tham số end để thay đổi hoặc loại bỏ ký tự xuống dòng này
## để đặt chuỗi chứa dấu ngoặc đơn, cần dùng chuỗi thoát để tránh nhầm lẫn điểm bắt đầu và kết thúc chuỗi
## dấu ngoặc đơn bên trong chuỗi được viết bằng ký tự thoát ' với dấu gạch chéo ngược phía trước
## ví dụ, chuỗi 'What's your name?' cho phép python hiểu đúng nội dung chuỗi
## một cách khác là dùng dấu ngoặc kép bao quanh chuỗi chứa dấu ngoặc đơn
## ương tự, nếu chuỗi dùng dấu ngoặc kép thì phải dùng chuỗi thoát " để biểu diễn dấu ngoặc kép bên trong
## dấu gạch chéo ngược \ được dùng để biểu diễn chính ký tự gạch chéo ngược
## để tạo chuỗi nhiều dòng, có thể dùng dấu ngoặc kép ba lần hoặc dùng ký tự thoát xuống dòng \n
## việc chỉ dùng các hằng số cố định sẽ nhanh chóng trở nên hạn chế khi viết chương trình
## để lưu trữ và thao tác với dữ liệu, python sử dụng biến
## biến đúng như tên gọi của nó, giá trị của biến có thể thay đổi trong quá trình chương trình chạy
## bạn có thể lưu trữ bất kỳ thông tin nào vào một biến
## biến đại diện cho một vùng nhớ trong máy tính dùng để lưu dữ liệu
## khác với hằng số, biến cần có tên để có thể truy cập và sử dụng lại
## việc đặt tên cho biến giúp chương trình dễ đọc và dễ hiểu hơn
## biến là một ví dụ của định danh trong python
## định danh là tên được dùng để xác định một đối tượng nào đó trong chương trình
## ký tự đầu tiên của định danh phải là chữ cái hoặc dấu gạch dưới
## chữ cái có thể là chữ hoa ascii, chữ thường ascii hoặc ký tự unicode
## các ký tự tiếp theo có thể là chữ cái, chữ số hoặc dấu gạch dưới
## định danh không được bắt đầu bằng chữ số
## tên định danh phân biệt chữ hoa và chữ thường
## ví dụ myname và myName là hai định danh khác nhau
## ví dụ về định danh hợp lệ i là name_2_3
## ví dụ về định danh không hợp lệ gồm 2things, this is spaced out, my-name và >a1b2_c3
## biến có thể lưu trữ các giá trị thuộc nhiều kiểu dữ liệu khác nhau
## các kiểu dữ liệu cơ bản trong python là số và chuỗi
## những kiểu dữ liệu này đã được trình bày ở các chương trước
## chương trình bắt đầu bằng việc gán giá trị hằng số 5 cho biến i bằng toán tử gán =
## âu lệnh gán này dùng để liên kết tên biến i với giá trị 5
## tiếp theo, chương trình dùng câu lệnh print để in giá trị hiện tại của biến i ra màn hình
## sau đó, chương trình cộng thêm 1 vào giá trị đang lưu trong biến i
## giá trị mới này được gán lại cho chính biến i
## tiếp theo, câu lệnh print được dùng để in giá trị mới của biến i
## kết quả nhận được là 6, đúng với giá trị sau khi đã cộng thêm 1
## sau đó, một chuỗi ký tự nhiều dòng được gán cho biến s
## chương trình in nội dung của biến s ra màn hình
## trong python, biến được sử dụng bằng cách gán trực tiếp giá trị cho chúng
## không cần khai báo trước hay định nghĩa kiểu dữ liệu cho biến
## dòng lệnh vật lý là những dòng  nhìn thấy trực tiếp khi viết mã trong trình soạn thảo
## dòng lệnh logic là những gì python hiểu là một câu lệnh hoàn chỉnh
## mặc định, python coi mỗi dòng lệnh vật lý tương ứng với một dòng lệnh logic
## ví dụ, câu lệnh print('hello world') nếu viết trên một dòng thì vừa là dòng vật lý vừa là dòng logic
## python khuyến khích mỗi dòng vật lý chỉ chứa một dòng logic để mã dễ đọc
## nếu muốn viết nhiều dòng logic trên cùng một dòng vật lý, phải dùng dấu chấm phẩy để ngăn cách
## các cách viết như i = 5; print(i) đều hợp lệ và cho kết quả giống nhau
## tuy nhiên, không nên sử dụng dấu chấm phẩy trong python vì làm mã khó đọc
## trong thực tế, hầu như không ai dùng dấu chấm phẩy trong chương trình python
## khi một dòng mã quá dài, có thể chia thành nhiều dòng vật lý bằng dấu gạch chéo ngược
## cách này được gọi là nối dòng tường minh
## ví dụ, một chuỗi dài có thể được nối qua nhiều dòng bằng dấu gạch chéo ngược
## python cũng hỗ trợ nối dòng ngầm định
## nối dòng ngầm định xảy ra khi dòng logic nằm trong dấu ngoặc đơn, ngoặc vuông hoặc ngoặc nhọn chưa đóng
## trong trường hợp này, không cần dùng dấu gạch chéo ngược để xuống dòng
## khoảng trắng trong python rất quan trọng, đặc biệt là khoảng trắng ở đầu dòng
## khoảng trắng ở đầu dòng được gọi là thụt lề
## python dùng thụt lề để xác định mức độ và phạm vi của các câu lệnh
## ác câu lệnh có cùng mức thụt lề sẽ được xem là thuộc cùng một nhóm
## mỗi nhóm câu lệnh như vậy được gọi là một khối lệnh
## khối lệnh dùng để thể hiện các phần mã đi cùng nhau trong chương trình
## 3nếu thụt lề sai, chương trình sẽ báo lỗi và không thể chạy
## chỉ cần thừa hoặc thiếu một dấu cách ở đầu dòng cũng có thể gây lỗi
## lỗi thường gặp là IndentationError, cho biết thụt lề không hợp lệ
## python không cho phép tự ý tạo khối lệnh mới nếu không đúng cú pháp
## các khối lệnh hợp lệ sẽ được giới thiệu ở các phần như luồng điều khiển
## cách thụt lề được khuyến nghị trong python là dùng bốn dấu cách
## cần sử dụng số dấu cách thụt lề nhất quán trong toàn bộ chương trình
## python không dùng dấu ngoặc nhọn để tạo khối lệnh mà chỉ dùng thụt lề
