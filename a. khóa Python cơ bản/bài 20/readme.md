## làm việc với file trong python ; đọc , ghi , xử lý encoding 
# làm việc với .txt 
f = open('md.txt','r')  // đây là gọi file lên làm việc  , r ở đây là reading chỉ đc để đọc 
print (f.mode)  // đưa ra thuộc tính 
f.close() // mở ra mà không đóng lại sẽ gây rò rỉ tài nguyên và dữ liệu không được ghi lại đúng cách 

- python sử dụng một cơ chế gọi là context manager (quản lý ngữ cảnh ) , nó giúp quản lý tài nguyên một cách an toàn và hiệu quả , đặc biệt là khi làm vc với các tệp hoặc có tài nguyên cần đóng lại sau khi sử dụng 
- with là một cơ chế trong python để quản lý tài nguyên một cách tự động và an toàn , giúp đảm bảo tài nguyên được giải phóng đúng cách khi không cần thiết 

with open('md.txt','r') as file : // đây là mở tệp rồi gán biến open('md.txt','r') vào file 
    print (file.closed)
    
print(file.closed)
  // nó sẽ tự động đóng file cho mình khi thoát khỏi dòng con của nó 


# endcoding 
encoding (mã hóa kí tự ) là cách chuyển đổi các kí tự thành một chuỗi các bit để máy tính lưu trữ và xử lý chúng 
máy tính chỉ hiểu và làm việc với các số dạng nhị phân . 
ascii - không lưu được các kí tự phức tạp và icon chỉ lưu đc tiếng anh 
utf-8 lưu đc hầu hết các kí tự 
utf-16 cải tiên và dùng nhiều dung lượng hơn utf-8

with open('md.txt','r',encoding='utf-8') as file : // mã hóa bằng utf-8 rồi đọc file md.txt
    data = file.read () // có thể chuyển cách đọc khác như từ read sang readline 
    print (data)

with open('md.txt','r',encoding='utf-8') as file :
    data = file.read (10) // 10 là sẽ in từ kí tự đầu kến kí tự thứ 10 
    print (data,end='')
    
with open('md.txt','r',encoding='utf-8') as file :
    size_to_read = 1000
    data = file.read(size_to_read)
    while data :
       print ( data,end='')
       data = file.read(size_to_read) // nó đọc dữ liệu cho mình rồi in ra thành từng dòng 

# chỉnh sửa file 
with open('test_demo.txt','w',encoding='utf-8') as file : // w vào chế độ ghi đè , nếu chưa có file test_demo.txt thì sẽ tự tạo 
     file.write ( 'test')// dữ liệu ghi thêm là test 

with open('test_demo.txt','a',encoding='utf-8') as file : //ghi tiếp tục vào cuối file
     file.write ( 'demo')
     file.flush()  //dùng để dữ liệu được đẩy hết vào file
