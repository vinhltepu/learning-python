## tìm hiểu về module csv
# khái niệm 
module csv dùng để đọc và ghi các tệp  csv ( comma separated values ) ,là một định dạng văn bản đơn giản với các giá trị được phân tách bằng dấu phẩy (hoặc dấu phân cách khác )

# đọc dữ liệu từ file csv lên chương trình 
# csv.reader(): đọc csv , trả về dưới dạng danh sach 
vd1 
import csv 
with open ('data.csv','r',encoding='utf-8') as file :
   data = csv.reader(file)
   print (next(data)) // in 1 dòng có trong file 


vd2
import csv 
with open ('data.csv','r',encoding='utf-8') as file :
   data = csv.reader(file)
   for data in datas  /// in toàn bộ các dòng trong danh sách , trong file 
      print(data[0:2]) /// in cột 1 và 2 của dang sách ra 
      