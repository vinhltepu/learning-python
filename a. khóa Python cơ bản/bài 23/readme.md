## xử lý lỗi bằng Try-Except
# syntax 
try:
    pass
except:
    pass
elsae:
    pass 
finally:
    pass


#  try: đặt mã lệnh có thể gây ngoại lệ ở đây 
# except : bắt và xử lý các ngoại lệ khi chúng xảy ra 
# else : thực thi nếu không có ngoại lệ nào xảy ra trong khối try 
# finally: thực thi cuối cùng , bất kể có xảy ra ngoại lệ hay không 
vd1
print ('chương trình bắt đầu chạy ' )
try:
    resulf =1/0 
    print(resulf)
except Exeption as e :
    print ('lỗi ở đây ',e)
print ('chương trình kết thúc ')


vd2
print('Chương trình bắt đầu chạy')
try:
    result = 1/1
    print(result)
    print(c)
except ZeroDivisionError: // dùng để bắt lỗi chia cho 0
    print('Lỗi cấp 1')
except Exception: // là bắt lỗi tổng quát. Nó thường dùng để xử lý các lỗi còn lại mà bạn không chỉ rõ riêng từng loại
    print('Lỗi cấp 2')
print('Chương trình kết thúc')
vd3
print('Chương trình bắt đầu chạy')
try:
    result = 1/1
    print(result)
except ZeroDivisionError:
    print('Lỗi cấp 1')
except Exception: 
    print('Lỗi cấp 2')
else:
    print('không có lỗi nào trong khối lệnh try')
print ('chương trình kết thúc ')

vd4
print('Chương trình bắt đầu chạy')
try:
    result = 1/1
    print(result)
except ZeroDivisionError:
    print('Lỗi cấp 1')
except Exception: 
    print('Lỗi cấp 2')
else:
    print('không có lỗi nào trong khối lệnh try')
finally:
    print('đoạn này chạy kể cả có lỗi hay không)
print ('chương trình kết thúc ')
 
# raise dùng để ném một ngoại lệ 
print('Chương trình bắt đầu chạy')
try:
    result = 1/1
    print(result)
    raise Exception
except ZeroDivisionError:
    print('Lỗi cấp 1')
except Exception: 
    print('Lỗi cấp 2')
print ('chương trình kết thúc ')

