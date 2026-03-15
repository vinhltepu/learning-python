# Khái niệm first-class function (hàm bậc nhất) trong lập trình đề cập đến việc hàm có thể được xử như một đối tượng "bậc nhất"
1. Hàm có thể được gán cho một biến.
vd
def hi ( ) : 
   print('xin chao ')
demo = hi 
demo ()

2. Hàm có thể được truyền như đối số cho một hàm khác
def hi ( ) : 
   print('xin chao ')
def outter_func(func): // hàm outter_func nhận vào 1 func và sẽ thực thi hàm đó trong hàm này đó gọi là chuyển đổi số 
    func()
outter_func(hi)

3. Hàm có thể trả về từ một hàm khác.
def outter_func(func):
    message = 'Đây là outter_function'

    def inner_func():
        print(message)

    return inner_func
4. Hàm có thể được lưu trữ trong một cấu trúc dữ liệu
def hi():
    print('Xin chào')


list_func: list = [hi, hi, hi, hi]

for func in list_func:
    func()

# closure xảy ra khi một hàm được định nghĩa bên trong một hàm khác và hàm bên trong truy cập và sử dụng các biến từ phạm vi bên ngoài nó (phạm vi của hàm chứa).

Đặc điểm của closure trong Python:
- Hàm bên trong có thể truy cập các biến của hàm bên ngoài (hàm chứa nó).
- Hàm bên trong có thể "nhớ" các giá trị của các biến từ phạm vi bên ngoài, ngay cả khi hàm bên ngoài đã thực thi xong.
vd 
def ham_ngoai():
    number = 1
    def ham_trong():
        nonlocal number
        print(number)
        number = number + 1
    return ham_trong
test = ham_ngoai()
test()
test.__name // in ra tên 

# Decorator trong Python nó cho phép bạn thay đổi hoặc mở rộng hành vi của một hàm hoặc lớp mà không cần thay đổi mã nguồn của chúng. Decorator thực chất là một hàm nhận vào một hàm khác làm đối số và trả về một hàm mới.
Cách thức hoạt động của decorator:
Hàm decorator là một hàm nhận một hàm khác làm đối số.
Hàm decorator sẽ "quấn" (wrap) hàm ban đầu và trả về một hàm mới.
Khi gọi hàm ban đầu, bạn thực sự đang gọi hàm đã được "quấn" bởi decorator.

def decorator_func(func): // tạo hàm 

    def wrap(): // định nghĩa 1 hàm khác 
        print ('hàm wrap đang chạy')
        func() // thực thi hàm truyền vào đầu tiên 
        print ('hàm wrap chạy thành công')

    return wrap
def test() :
    print ( 'xin chao ')
demo = (decorator_func(test))
demo ( )

# decoratỏ lồng nhau 
khi sử dụng nhiều deccorator cho một hàm , bạn có thể áp dụng chúng theo thứ tự từ ngoài vào trong 

cách sử dụng : 
nếu bạn có nhiều decorator , python sẽ áp dụng theo thứ tự từ dưới lên ( tức là decorator cuối cùng được áp dụng đầu tiên )

def decorator_1(func):

    def wrap():
        print('Hàm decorator 1 đang chạy')
        func()
        print('Hàm decorator 1 kết thúc ')

    return wrap

def decorator_2(func):

    def wrap():
        print('Hàm decorator 2 đang chạy')
        func()
        print('Hàm decorator 2 kết thúc ')

    return wrap

def demo ()
    print ( ' hàm demo sẽ được trang trí ')

test =decorator_2(decorator_1(demo)) // chạy sẽ là hàm 2 chạy - hàm 1 chạy - demo - hàm 1 kết thúc - hàm 2 kết thúc 

# truyền tham số cho decorator 
def decorator_func(func):

    def wrap():
        print('wrap đang chạy ')
        func()
        print('wrap kết thúc  ')
def demo () :
    print ( ' đang học decorator')

test = decorator_func(demo)

test ( )

