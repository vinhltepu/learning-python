# khái niệm về sessoion 

Được lưu trên server (thường có Session ID gửi qua Cookie).
Dùng để lưu thông tin tạm thời trong phiên làm việc của user, như đăng nhập.
Hết thời gian hoặc đóng trình duyệt thì session thường bị xóa.
Bảo mật hơn cookie vì không lưu thông tin trực tiếp trên client

# - Cookie:
+ Được lưu trên trình duyệt của người dùng.
+ Dùng để lưu thông tin như token đăng nhập, tùy chọn giao diện, giỏ hàng...
+ Có thể được gửi lên server mỗi lần request.
+ Có thời gian sống do server hoặc client đặt ra.





1. Client gửi request lên server => flash("Xin chào tôi đang học web development") => set-cookie
server response về client
Cái session đấy tồn tại cho tới khi nào mà bên phía server sử dụng cái function get_flashed_messages()

2. client gửi request tới server thì bên phía server nhận dc request => cookie (session)
server sử dụng function get_flashed_messages() => thì nó sẽ lấy hết các nội dung trong phần cookie (session mà client gửi tới)
Thì server sẽ xử lí => server tạo response và trong cái response đấy server sẽ xóa cookie (session) đi rồi phản hồi về clien
