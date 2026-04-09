## Lập trình hướng đối tượng
# Object Oriented Programming
đây được gọi là phương pháp lập trình hướng thủ tục
đây được gọi là mô hình lập trình hướng đối tượng
lớp và đối tượng là hai khía cạnh chính của lập trình hướng đối tượng
một lớp tạo ra một kiểu dữ liệu mới trong đó các đối tượng là các thể hiện của lớp đó
lưu ý rằng ngay cả các số nguyên cũng được coi là đối tượng của lớp int
các đối tượng có thể lưu trữ dữ liệu bằng cách sử dụng các biến thông thường thuộc về đối tượng đó
các biến thuộc về một đối tượng hoặc lớp được gọi là trường field
các hàm như vậy được gọi là phương thức method của lớp
nói chung các trường và phương thức có thể được gọi là thuộc tính attributes của lớp đó
các trường có hai loại chúng có thể thuộc về mỗi thể hiện đối tượng của lớp hoặc chúng có thể thuộc về chính lớp đó
chúng được gọi tương ứng là biến thể hiện và biến lớp
một lớp được tạo bằng class từ khóa

# The self 
các phương thức lớp có thêm một tham số đầu tiên mà khi gọi phương thức không cần truyền giá trị
python sẽ tự động cung cấp giá trị cho tham số này
tham số này tham chiếu đến chính đối tượng đó và theo quy ước được đặt tên là self
mặc dù có thể đặt tên khác nhưng khuyến nghị sử dụng tên chuẩn self
việc sử dụng tên self giúp người đọc dễ hiểu và ide hỗ trợ tốt hơn
trong python self tương đương với this trong c++ java và c#
khi gọi phương thức python sẽ tự động truyền đối tượng vào tham số self
myobject.method(arg1 arg2) sẽ được python chuyển thành MyClass.method(myobject arg1 arg2)
self đại diện cho đối tượng đang gọi phương thức
ngay cả khi phương thức không có tham số nào khác thì vẫn phải có tham số self

# Classes
lớp đơn giản nhất có thể được tạo bằng câu lệnh class và tên lớp
thân của lớp là một khối thụt lề và có thể để trống bằng pass
đối tượng được tạo bằng cách gọi tên lớp kèm theo cặp dấu ngoặc đơn
đối tượng tạo ra là một thể hiện của lớp đó
in đối tượng ra màn hình cho biết nó thuộc lớp nào và mô đun nào
python hiển thị cả địa chỉ bộ nhớ nơi đối tượng được lưu trữ
địa chỉ bộ nhớ này có thể khác nhau trên mỗi máy tính

# Methods
các lớp và đối tượng có thể có các phương thức giống như hàm
phương thức khác hàm ở chỗ có thêm tham số self
phương thức được định nghĩa bên trong lớp bằng từ khóa def
đối tượng có thể gọi phương thức thông qua dấu chấm
khi gọi phương thức python tự động truyền đối tượng vào self
say_hi không nhận tham số nào khác nhưng vẫn phải có self trong định nghĩa
có thể gọi phương thức bằng cách tạo đối tượng trực tiếp rồi gọi phương thức

# The __init__ method 
init là một phương thức đặc biệt trong lớp python
phương thức init được gọi tự động khi đối tượng được tạo
init dùng để khởi tạo các giá trị ban đầu cho đối tượng
tên init có hai dấu gạch dưới ở đầu và cuối
init luôn có tham số self và có thể có thêm các tham số khác
trong init có thể tạo các trường của đối tượng bằng self.tentruong
self.name và name là hai biến khác nhau
self.name là biến thuộc về đối tượng
name là biến cục bộ của phương thức
khi tạo đối tượng bằng p = Person('Swaroop') thì init được gọi tự động
không cần gọi init một cách trực tiếp
các phương thức khác có thể sử dụng các trường đã được khởi tạo bằng self.name

# Class And Object Variables 
biến và trường dữ liệu là các biến được liên kết với lớp và đối tượng
các biến này chỉ tồn tại trong không gian tên của lớp hoặc đối tượng
có hai loại trường dữ liệu là biến lớp và biến đối tượng
biến lớp thuộc về lớp và được chia sẻ cho tất cả các thể hiện
chỉ có một bản sao của biến lớp
khi một đối tượng thay đổi biến lớp thì các đối tượng khác đều thấy sự thay đổi
biến đối tượng thuộc về từng thể hiện riêng lẻ
mỗi đối tượng có bản sao riêng của biến đối tượng
biến đối tượng không được chia sẻ giữa các đối tượng
population là biến lớp của robot
name là biến đối tượng được gán bằng self.name
biến lớp nên được truy cập bằng tenlop.tentruong
biến đối tượng được truy cập bằng self.tentruong
biến đối tượng trùng tên sẽ che khuất biến lớp
có thể truy cập biến lớp bằng self.class.tentruong
how_many là phương thức lớp vì làm việc với biến lớp
phương thức lớp được khai báo bằng decorator classmethod
decorator là hàm bao bọc giúp thay đổi hành vi của hàm
init được dùng để khởi tạo dữ liệu ban đầu cho đối tượng
self.name là dữ liệu riêng cho từng đối tượng
các thuộc tính và phương thức của đối tượng được truy cập bằng dấu chấm
docstring được dùng để mô tả lớp và phương thức
có thể truy cập docstring bằng tenlop.doc
các thành viên của lớp mặc định là public
tên bắt đầu bằng hai dấu gạch dưới sẽ được xem là private
quy ước dùng một dấu gạch dưới cho biến nội bộ
quy ước này không bắt buộc trong python
trong python tất cả phương thức đều là virtual

# Inheritance
lập trình hướng đối tượng giúp tái sử dụng mã thông qua cơ chế kế thừa
kế thừa thể hiện mối quan hệ lớp cha và lớp con
các lớp có đặc điểm chung nên được gom vào một lớp cơ sở
các lớp con kế thừa lại đặc điểm chung từ lớp cha
việc thay đổi lớp cha sẽ tự động ảnh hưởng đến các lớp con
thay đổi trong một lớp con không ảnh hưởng đến lớp con khác
có thể xem đối tượng lớp con như một đối tượng lớp cha
điều này được gọi là đa hình
đa hình cho phép lớp con thay thế lớp cha khi cần
kế thừa giúp tránh lặp lại mã nguồn
schoolmember là lớp cơ sở
teacher và student là các lớp con
lớp con kế thừa bằng cách đặt tên lớp cha trong ngoặc sau tên lớp
khi lớp con có init riêng thì phải gọi init của lớp cha thủ công
nếu lớp con không có init thì python tự động gọi init lớp cha
lớp con có thể ghi đè phương thức của lớp cha
python luôn ưu tiên tìm phương thức trong lớp con trước
nếu không có thì mới tìm trong lớp cha
có thể sử dụng lại một phần phương thức lớp cha trong lớp con
nhiều lớp cha trong kế thừa được gọi là đa kế thừa
tham số end trong print dùng để in tiếp trên cùng một dòng