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
      
 giải nén list 
import csv 
with open ('data.csv','r',encoding='utf-8') as file :
   data = csv.reader(file)
   for first_name , last_name, email in datas : 
     print (first_name , last_name, email)

# csv.writer() : ghi dữ liệu vào csv 
#  .writerow : ghi một dòng vào tệp csv 
# delimiter 
import csv 
data = ['a','b','c']
with open ('data.csv','w',encoding='utf-8,newline='') as file_write : // newline là hk cho xuống dòng , và sẽ hk bị trống 1 dòng ở giữa 
   csv_write=csv.write(file_write,delimiter='@') // delimiter là thay đổi giá trị phân cách giữa các giá trị 
   csv_write.writerow(data)

# quotechar
import csv 
data = ['a','b','c']
with open ('data.csv','w',encoding='utf-8,newline='') as file_write : 
   csv_write=csv.write(file_write,quoctechar='!')  // quoctechar là giá trị bao bọc 
   csv_write.writerow(data)

# .writerows() ; ghi nhiều dòng vào tệp csv 
import csv 
data = [
   ['a','b','c'],
   [1,2,3],
   ['demo','test','check']  // cụm data này gọi là mảng 2 chiều 
]
with open ('data.csv','w',encoding='utf-8,newline='') as file_write : 
   csv_write=csv.write(file_write,)  
   csv_write.writerows(data)


# csv.DictReader : đọc tệp csv và trả về mỗi dòng dưới dạng từ điển 
import csv 
with open ('data.csv','r',encoding='utf-8,newline='') as file :
   data=csv.reader(file)
   for data in datas : 
      print(data) // print(data['firts_name']) nếu muốn in mỗi dòng đầu có thể thay thế firts_name bằng những dòng khác 

# csv.DictWriter : ghi dữ liệu vào tệp dưới dạng từ điển 
import csv 
data = {'full_name':'nguyen van a ','age':'21'}
with open ('demo.csv','w',encoding='utf-8,newline='') as file_writer :
   keys = ['full_name','age']
   csv_ writer = csv.DictWriter(file_writer,fieldnames = keys)
   csv_ writer.writeheader()
   csv_ write.writerow(data)

# copy file data.csv sang 1 file mới
import csv
with open('data.csv', 'r', encoding='utf-8') as file_read: // mở fiel cũ để đọc 
    csv_read = csv.reader(file_read)
    with open("data_coppy.csv", 'w', encoding='utf-8') as file_write: // mở file mới để ghi lấy dữ liệu sang file data_coppy.csv
        csv_write = csv.writer(file_write)

        for data in csv_read:
            csv_write.writerow(data)


