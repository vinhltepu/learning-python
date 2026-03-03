# hướng dẫn làm việc với mô đun date time 
module datetime là một thư viện tiêu chuẩn trong Python , được sử dụng để làm việc với ngày và giờ . Nó cung cấp các lớp và phương thức hỗ trợ bạn trong việc quản lý thời gian , tính toán các khoảng thời gian , và chuyển đổi các định dạng thời gian khác nhau 

# date 
vd:
import datetime 

d= datetime.date (2026,3,3)
print (d)
print (d.weekday()) // trả về từ 0-6 tương ứng 0 là thứ 2 ... 6 là chủ nhật 
print (d.isoweekday) // trả về 1-7 tương ứng 1 là thứ 2 ... 7 là chủ nhật 

d = datetime.date (2026,3,3)
t_delta =datetime.timedelta(days=2)
new_d = d + t_delta // ngày tính theo công thức này sẽ này ngày hiện tại 3/3 + thêm 2 ngày nữa, có thể thay thế bằng + - x :
print (new_d)


# time 
t = datetime.time(20,32,13,2000) // tương ứng 20 giờ 32 phút 13 giây 2000 micro giây 
print (t) // hiển thị giờ phút giây là 20h 32p 13s , nếu như mà t.hour sẽ hiển thị giờ và tương tự với phút giây 


# datetime
dt = datetime.datetime(2026,3,3,20,34,32,3000)
print ( dt.date ()) // trả về ngày tháng năm 
print (dt.time()) // trả về giờ phút giây micro giây 
print (dt) // hiển thị thông tin từ năm đến micro giây 

dt = datetime.datetime(2026,3,3,20,34,32,3000)
t_delta = datetime.timedelta(days=3,month=2) //  có thể thay thế days bằng second,year...
print (dt + t_delta) // in ra ngày tháng năm trên kia cộng thêm 3 ngày và tháng cộng thêm 2 

# time zone 

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utc = datetime.datetime.utc(date.time.timezone.utc)

// mục đích : trả về thời gian hiện tại ở utc , không phụ thuốc vào múi giờ hệ thống . thời gian này không thay đổi theo múi giờ , mà luôn cố định với utc 
// đây là thời gian chuẩn quốc tế (utc) không phụ thuộc múi giờ , rất hữu ích khi đồng bộ hóa thời gian giữa các hệ thống hoặc quốc gia khác nhau 
// timezone việt nam +7

print (dt_today)
print (dt_now)
print (dt_utc)

# tra timezone 
import zoneinfo 
tz= zoneinfo.available_timezone() // hiện thị tất cả các múi giờ trên thế giới  
print(tz)

# kiểm tra thời gian thực lệch utc bao nhiêu 
import zoneinfo 
tz= zoneinfo.ZoneInfo('Asia/Ho_Chi_Minh')
dt_1=datetime.datetime(2026,3,3,tzinfo=tz) 
print(dt_vietnam.astimezone(tz))


# timestamp
-Là một giá trị đại diện cho một thời diểm cụ thể trong thời gian , thường được biểu diễn ơ số nguyên và thập phân , giá trị này mô tả số giay đã trôi qua kể từ 1 thời điểm cố định gọi là epoch time
- trong hệ thống Unix và Linux , thời điểm cố định là 1 tháng 1 năm 1970 ,00:00:00 UTC vì thế timestamp được gọi là  một số nguyên thể hiện số giây đã trôi qua từ thời điểm này 
-timestamp ( unix timestamp) thường dược tính dựa vào utc hay gmt , và nó k bị ảnh hưởng bởi múi giờ 


dt = datetime.datetime(2026,3,3)
ts = dt.timestamp 
print (ts)//hiển thị thời gian ra giây tính từ 1/1/1970
print (datetime.datetime.fromtimestamp(17982826368.0)) // hiển thị thời gian ra ngày và giờ 