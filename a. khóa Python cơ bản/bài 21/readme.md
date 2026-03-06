## tìm hiểu về module random
# khái niệm 
module random là thư viện chuẩn cung cấp các hàm để thực hiện các thao tác liên quan đến việc sinh số ngẫu nhiên , có thể sử dụng nó để tạo các số ngẫu nhiên , lựa chọn ngẫu nhiên từ một dãy giá trị , trộn các phần tử trong 1 danh dách 

# random.random() trả về một số thực ngẫu nhiên trong khoảng (0.0,1.0)
import random
random.random() 
print(random.random())// kết quả ngẫu nhiên 0.0-1.0 

# random.uniform() trả về một số thực ngẫu nhiên trong khoảng [a,b)
import random
random.uniform() 
print(random.random(0,10)) 

# random.randit() trả về một số nguyên từ [a,b] (bao gồm cả a và b )
import random
print(random.randit(1,6))

# random.choie(sequence) chọm ngẫu nhiên một phần tử từ 1 dãy ( list ,tuple,etc)
import random
list_color = ['đỏ','xanh','vàng' ]
print(random.choice(list_color))

# random.choies() cho phép bạn lấy ngẫu nhiên các phần tử từ 1 dãy ( list ,tuple,etc)và hỗ trợ thêm tham số weights
import random
list_color = ['đỏ','xanh','vàng' ]
random(choies(list_color,k=2,weights=[0.4,0.4,0.2])) // k là phần tử có thể thay thế được k=2 là lấy ngẫu hiên 2 lần weight là phần trăm ưu tiên được chọn nhiều hơn 

# random.shuffle(sequence) trộn ngẫu nghiên các phần tử có trong danh sach 
import random
desk = [i for i in range (1,50)]
random.shuffle(desk)
print(desk)

# random.sample(sequence ,  k) chọn nhẫu nhiên k phần tử từ dãy mà không trùng lặp 
import random
desk = [i for i in range (1,50)]
data = random.sample(desk , k = 10)
print(data) // lấy ngẫu nhiên 10 số mà không trùng lặp 

