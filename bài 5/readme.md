## functions
# chức năng 
hàm là các đoạn mã chương trình có thể tái sử dụng
hàm cho phép đặt tên cho một khối lệnh và gọi lại nhiều lần
việc sử dụng hàm giúp tránh viết lặp lại mã
gọi hàm là việc chạy khối lệnh của hàm bằng tên hàm
python có nhiều hàm tích hợp sẵn như len và range
hàm là thành phần rất quan trọng trong chương trình phức tạp
hàm được định nghĩa bằng từ khóa def
sau def là tên hàm dấu ngoặc tròn và dấu hai chấm
khối lệnh của hàm phải được thụt lề
hàm có thể không có tham số
có thể gọi một hàm nhiều lần mà không cần viết lại mã

# tham số hàm 
một hàm có thể nhận các tham số là các giá trị mà cung cấp cho hàm
các tham số này giống như các biến ngoại trừ giá trị của chúng được xác định khi gọi hàm
các tham số được chỉ định trong cặp dấu ngoặc đơn trong định nghĩa hàm
khi gọi hàm chúng ta cung cấp các giá trị theo cùng một cách
tên trong định nghĩa hàm được gọi là tham số
các giá trị cung cấp khi gọi hàm được gọi là đối số
chúng ta định nghĩa một hàm sử dụng hai tham số a và b
chúng ta tìm số lớn hơn bằng một câu lệnh if elif else đơn giản
lần đầu gọi hàm chúng ta trực tiếp cung cấp các số làm đối số
lần thứ hai chúng ta gọi hàm với các biến làm đối số
giá trị của đối số x được gán cho tham số a
giá trị của đối số y được gán cho tham số b
hàm hoạt động giống nhau trong cả hai trường hợp

# biến cục bộ 
khi khai báo biến bên trong định nghĩa hàm chúng không liên quan đến các biến cùng tên bên ngoài hàm
tên biến chỉ có phạm vi cục bộ trong hàm đó
điều này được gọi là phạm vi của biến
tất cả các biến đều có phạm vi của khối lệnh mà chúng được khai báo
phạm vi bắt đầu từ điểm định nghĩa tên biến
lần đầu in giá trị của x trong hàm python sử dụng giá trị của tham số được truyền vào
khi gán giá trị mới cho x trong hàm thì x chỉ thay đổi trong phạm vi hàm
biến x được định nghĩa trong khối chính không bị ảnh hưởng
câu lệnh print cuối cùng cho thấy giá trị x không bị ảnh hưởng bởi phép gán cục bộ bên trong hàm được gọi trước đó

# The global statement
nếu muốn gán giá trị cho một biến được định nghĩa ở cấp cao nhất của chương trình thì phải cho python biết đó là biến toàn cục
biến toàn cục là biến không nằm trong bất kỳ phạm vi nào như hàm hoặc lớp
chúng ta thực hiện điều này bằng cách sử dụng câu lệnh global
không thể gán giá trị cho biến được định nghĩa bên ngoài hàm mà không dùng global
 có thể sử dụng giá trị của biến bên ngoài hàm nếu không có biến cùng tên bên trong hàm
việc này không được khuyến khích vì làm chương trình khó hiểu
sử dụng global giúp làm rõ rằng biến được định nghĩa ở khối lệnh ngoài cùng
câu lệnh global khai báo rằng biến là biến toàn cục
khi gán giá trị cho biến toàn cục trong hàm thì giá trị đó cũng thay đổi ở khối chính
có thể khai báo nhiều biến toàn cục trong cùng một câu lệnh global

# giá trị đối số mặc định 
giá trị đối số mặc định cho phép đặt một số tham số là tùy chọn và sử dụng giá trị mặc định khi không cung cấp giá trị
giá trị đối số mặc định được chỉ định bằng cách dùng toán tử gán = trong định nghĩa hàm theo sau là giá trị mặc định
giá trị mặc định của tham số phải là hằng số và phải là bất biến
hàm say được dùng để in một chuỗi nhiều lần theo số thứ tự được chỉ định
nếu không cung cấp giá trị cho tham số times thì chuỗi sẽ chỉ được in một lần
chỉ những tham số nằm ở cuối danh sách tham số mới có thể được gán giá trị đối số mặc định
không thể có tham số có giá trị mặc định đứng trước tham số không có giá trị mặc định
các giá trị được gán cho tham số theo vị trí

# đổi số từ khóa 
có thể cung cấp giá trị cho các tham số đó bằng cách đặt tên cho chúng - điều này được gọi là đối số từ khóa 
việc sử dụng hàm dễ dàng hơn vì chúng ta không cần phải lo lắng về thứ tự của các đối số
có thể chỉ gán giá trị cho những tham số mà chúng ta muốn, miễn là các tham số khác có giá trị mặc định
Hàm có tên gọi này fun có một tham số không có giá trị mặc định, tiếp theo là hai tham số có giá trị mặc định.

# tham số VarArgs
số lượng đối số thay đổi, điều này có thể đạt được bằng cách sử dụng dấu sao (lưu dưới dạng function_varargs.py)
khi khai báo 1 tham số có dấu * ất cả các đối số vị trí từ điểm đó đến cuối sẽ được tập hợp lại thành một bộ gọi là 'param'
khi khai báo 1 tham số có 2 dấu ** thì tất cả các đối số từ khóa từ điểm đó đến cuối sẽ được tập hợp lại thành một từ điển có tên là 'param'

# câu lệnh return 
được sử dụng để thoát khỏi  một hàm 
cũng có thể tùy chọn trả về một giá trị từ hàm 
lưu dưới dạng function_return.py
hàm maximum trả về giá trị lớn nhất trong tham số 
sử dụng một if..elsecâu lệnh đơn giản để tìm giá trị lớn hơn và sau đó trả về giá trị đó
sử dụng câu lệnh return không có giá trị tương đương return None`.`. `.` Nonelà một kiểu dữ liệu đặc biệt trong Python biểu thị sự trống rỗng
mỗi hàm đều ngầm chứa một return Nonecâu lệnh ở cuối 
có thể thấy điều này bằng cách chạy print(some_function())hàm some_functionmà không sử dụng returncâu lệnh đó

# chuỗi tài liệu 
Python có một tính năng rất hữu ích gọi là chuỗi tài liệu , thường được gọi tắt là docstring 
Docstring là một công cụ quan trọng nên sử dụng vì nó giúp ghi chú chương trình tốt hơn và làm cho chương trình dễ hiểu hơn
có thể lấy lại docstring từ một hàm, ngay cả khi chương trình đang chạy
docstring là chuỗi ký tự ở dòng logic đầu tiên của một hàm
docstring cũng áp dụng cho module và lớp
quy ước docstring là chuỗi nhiều dòng dòng đầu viết hoa kết thúc bằng dấu chấm dòng thứ hai để trống và giải thích chi tiết từ dòng thứ ba
nên dùng docstring cho tất cả các hàm không tầm thường
có thể truy cập docstring của hàm bằng thuộc tính doc
python coi hàm cũng là đối tượng nên có thể truy cập thuộc tính của nó
hàm help() hiển thị docstring của hàm một cách gọn gàng
các công cụ tự động có thể trích xuất tài liệu từ docstring
nên sử dụng docstring để tài liệu hóa chương trìn
pydoc hoạt động tương tự như help() và sử dụng docstring