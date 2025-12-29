# cấu trúc dữ liệu 
cấu trúc dữ liệu là những cấu trúc có thể chứa một số dữ liệu lại với nhau 
chúng được sử dụng để lưu trữ một tập hợp dữ liệu có liên quan

# danh sách( list )
danh sách listlà một cấu trúc dữ liệu chứa một tập hợp các mục được sắp xếp theo thứ tự
có thể lưu trữ một chuỗi các mục trong một danh sách
danh sách các mục cần được đặt trong dấu ngoặc vuông để Python hiểu rằng bạn đang chỉ định một danh sách
sau khi tạo danh sách, bạn có thể thêm, xóa hoặc tìm kiếm các mục trong danh sách
danh sách là một kiểu dữ liệu có thể thay đổi

# Quick Introduction To Objects And Classes
danh sách là một ví dụ về việc sử dụng đối tượng và lớp
Khi ta sử dụng một biến i và gán cho nó một giá trị, chẳng hạn như một số nguyên 5, ta có thể coi đó như việc tạo ra một đối tượng (tức là thể hiện) i của lớp (tức là kiểu dữ liệu) int.
Một lớp cũng có thể có các phương thức, tức là các hàm được định nghĩa chỉ để sử dụng đối với lớp đó
Ví dụ, Python cung cấp một append phương thức cho list lớp cho phép bạn thêm một mục vào cuối danh sách
Một lớp cũng có thể có các trường , thực chất chỉ là các biến được định nghĩa để sử dụng riêng cho lớp đó
shoplist là danh sách mua sắm của một người đi chợ
shoplist chỉ lưu trữ các chuỗi ký tự tên của các mặt hàng cần mua, nhưng bạn có thể thêm bất kỳ loại đối tượng nào vào danh sách, bao gồm cả số và thậm chí cả các danh sách khác
thêm một mục vào danh sách bằng cách sử dụng append phương thức của đối tượng danh sách
kiểm tra xem mục đó đã được thêm vào danh sách hay chưa bằng cách in nội dung của danh sách bằng cách đơn giản truyền danh sách printđó vào hàm in
khi  mua một mặt hàng trong chợ mà muốn xóa khỏi danh sách ta thực hiện bằng cách sử dụng câu lệnh del 
chỉ định mặt hàng nào trong danh sách mà mình muốn xóa và del câu lệnh sẽ tự động xóa nó khỏi danh sách 
nếu  muốn biết tất cả các phương thức được định nghĩa bởi đối tượng danh sách, hãy xem help(list) chi tiết

# tuple 
bộ dữ liệu (tuple) được sử dụng để kết hợp nhiều đối tượng lại với nhau
giống như list nhưng  không có chức năng mở rộng mà lớp danh sách cung cấp và không  thể sửa đổi bộ dữ liệu
các bộ dữ liệu (tuple) được định nghĩa bằng cách chỉ định các mục được phân tách bằng dấu phẩy bên trong một cặp dấu ngoặc đơn tùy chọn.
tuple thường được sử dụng trong trường hợp một câu lệnh hoặc một hàm do người dùng định nghĩa có thể giả định một cách an toàn rằng tập hợp các giá trị sẽ không thay đổi.
ta thấy rằng hàm len này có thể được sử dụng để lấy độ dài của bộ.
có thể truy cập các phần tử trong bộ dữ liệu bằng cách chỉ định vị trí của phần tử đó trong một cặp dấu ngoặc vuông.
một tuple rỗng được tạo bởi một cặp dấu ngoặc đơn rỗng.
một tuple chỉ chứa một phần tử thì phải chỉ định nó bằng dấu phẩy sau phần tử đầu tiên.
một bộ dữ liệu lồng trong một bộ dữ liệu khác không mất đi tính xác thực của nó.

# Dictionary
từ điển giống như một cuốn sổ địa chỉ, nơi bạn có thể tìm địa chỉ hoặc thông tin liên lạc của một người chỉ bằng cách biết tên của người đó
khóa phải là duy nhất
bạn chỉ có thể sử dụng các đối tượng bất biến cho khóa của từ điển
các cặp khóa và giá trị được chỉ định trong từ điển bằng cách sử dụng ký hiệu {key : value}
các cặp khóa-giá trị trong từ điển không được sắp xếp theo bất kỳ thứ tự nà
các từ điển mà bạn sẽ sử dụng là các thể hiện/đối tượng của lớp dict
chúng ta có thể xóa các cặp khóa-giá trị bằng cách sử dụng câu lệnh del
chúng ta truy cập từng cặp khóa-giá trị của từ điển bằng phương thức items
chúng ta có thể thêm các cặp khóa-giá trị mới bằng cách sử dụng toán tử truy cập chỉ mục
chúng ta có thể kiểm tra xem một cặp khóa-giá trị có tồn tại hay không bằng cách sử dụng toán tử in
để xem danh sách các phương thức của lớp dict, hãy xem help(dict)

# Sequence
danh sách, bộ dữ liệu và chuỗi là những ví dụ về dãy số
các tính năng chính là kiểm tra tư cách thành viên (in và not in) và các thao tác lập chỉ mục, cho phép truy xuất trực tiếp một mục cụ thể trong chuỗi
ba loại chuỗi được đề cập ở trên – danh sách, bộ dữ liệu và chuỗi ký tự – cũng có thao tác cắt lát cho phép trích xuất một phần của chuỗi
python bắt đầu đếm số từ 0
chỉ số cũng có thể là một số âm, trong trường hợp đó, vị trí được tính từ cuối chuỗi
thao tác cắt lát được thực hiện bằng cách chỉ định tên của chuỗi, theo sau là các số tùy chọn được phân tách bằng dấu hai chấm trong ngoặc vuông
vị trí bắt đầu được bao gồm nhưng vị trí kết thúc bị loại trừ khỏi chuỗi
neu số đầu tiên không được chỉ định, Python sẽ bắt đầu từ đầu chuỗi
nếu số thứ hai bị bỏ qua, Python sẽ dừng ở cuối chuỗi
shoplist[:] trả về một bản sao của toàn bộ chuỗi
có thể thực hiện cắt lát với các vị trí âm
có thể cung cấp tham số thứ ba cho lát cắt, đó là bước cắt (mặc định là 1)
khi bước nhảy là 2, ta nhận được các mục có vị trí 0, 2,…; khi bước nhảy là 3, ta nhận được các mục có vị trí 0, 3, 6
danh sách, bộ dữ liệu và chuỗi ký tự có thể được truy cập theo cùng một cách

# Tài liệu tham khảo 

Khi bạn tạo một đối tượng và gán nó cho một biến, biến đó chỉ tham chiếu đến đối tượng chứ không đại diện cho chính đối tượng đó
tên biến trỏ đến phần bộ nhớ máy tính nơi đối tượng được lưu trữ
điều này được gọi là liên kết tên với đối tượng
nếu bạn chỉ gán tên biến cho một tên khác, cả hai sẽ “tham chiếu” đến cùng một đối tượng
nếu bạn muốn sao chép một danh sách, chuỗi hoặc các đối tượng phức tạp, thì bạn phải sử dụng thao tác cắt lát để tạo bản sao
câu lệnh gán cho danh sách không tạo ra bản sao

# More About Strings
chuỗi ký tự cũng là đối tượng và có các phương thức thực hiện mọi thứ, từ kiểm tra một phần của chuỗi đến loại bỏ khoảng trắng
bạn đã sử dụng một phương thức của chuỗi rồi, chính là phương thức format()
các chuỗi ký tự mà bạn sử dụng trong chương trình đều là các đối tượng của lớp str
một số phương thức hữu ích của lớp này được minh họa trong ví dụ tiếp theo
để có danh sách đầy đủ các phương thức đó, hãy xem help(str)
Ở đây, chúng ta thấy rất nhiều phương thức xử lý chuỗi được sử dụng
startswith phương thức này được dùng để kiểm tra xem chuỗi có bắt đầu bằng chuỗi đã cho hay không
toán tử in được dùng để kiểm tra xem một chuỗi đã cho có phải là một phần của chuỗi hay không
phương thức find được sử dụng để xác định vị trí của chuỗi con đã cho trong chuỗi
find trả về -1 nếu không tìm thấy chuỗi con
lớp str cũng có một phương thức tiện lợi là join để lấy các phần tử của một chuỗi với chuỗi đóng vai trò là dấu phân cách giữa mỗi phần tử của chuỗi và trả về một chuỗi lớn hơn được tạo ra từ đó