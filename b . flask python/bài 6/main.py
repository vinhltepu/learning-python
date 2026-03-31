from click import clear
from flask import Flask, flash, make_response, redirect, render_template , request , session, url_for
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ABC123'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)  # thiết lập thời gian sống của session là 5 phút

@app.route('/')
def index():
    flash("xin chao mọi người")
    return render_template('index.html')

@app.route('/get-flash')
def get_flash():
    return get_flashed_messages()  # lấy tất cả các thông điệp flash đã được lưu trữ trong session và trả về chúng dưới dạng một danh sách. Các thông điệp này có thể được hiển thị cho người dùng trong giao diện của ứng dụng.

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login-page.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'admin123':

            session['account'] = username  # tạo session để lưu thông tin đăng nhập của người dùng 
            session['is_logged_in'] = True  # đánh dấu người dùng đã đăng nhập thành công

            session.permanent = True  # thiết lập session là vĩnh viễn (dựa trên PERMANENT_SESSION_LIFETIME)
            return render_template('manager-page.html')  # trả về trang quản lý nếu đăng nhập thành công    
        
        # cần tạo session nó vẫn nằm trong cái header của response nên nó sẽ được gửi về client và lưu trữ ở đó, khi client gửi request tiếp theo thì session sẽ được gửi kèm theo trong header của request đó, server sẽ kiểm tra session để xác định xem người dùng đã đăng nhập hay chưa và có quyền truy cập vào tài nguyên hay không.
        else:
            return 'Login failed'





@app.route('/delete-session')
def delete_session():
    session.clear()  # xóa session để đăng xuất người dùng khỏi hệ thống
    return redirect(url_for('login'))  # chuyển hướng về trang đăng nhập sau khi xóa session


@ app.route('/create-cookie')
def create_cookie():
    response = make_response('Cookie đã được tạo')
    response.set_cookie('demo', 'python',max_age=timedelta(minutes=5))  # tạo cookie với tên 'demo' và giá trị 'python'
    return response

@app.route('/get-cookie')
def get_cookie():  
    demo_cookie = request.cookies.get('demo')  # lấy giá trị của cookie 'demo' từ request
    return f'Giá trị của cookie "demo" là: {demo_cookie}'

@app.route('/delete-cookie')
def delete_cookie():    
    response = make_response('Cookie đã được xóa')
    response.set_cookie('demo', '', expires=0)  # xóa cookie bằng cách đặt giá trị rỗng và thời gian hết hạn là 0
    return response






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)

## client (Lúc đầu chưa có session)
# 1. Client gửi request tới server => Server response Client trang đăng nhập

# 2. Client gửi request tới server và kèm theo dữ liệu trong FORM => SERVER kiểm tra dữ liệu trong FORM
# Dữ liệu Trong Form được Server kiểm tra => chính xác bên server phản hồi về

# Header:
# HTTP/1.1 200 OK
# Set-Cookie: session=fjsfksdjhfsjkdhfksdfsjkf.SDKJFGSDFLJG, PATH=/; HTTPOnly
            # <account:tamdz>

# 3. Client gửi resquest tới server:

# REQUEST
# header:
# GET /login HTTP/1.1
# cookie: session=fjsfksdjhfsjkdhfksdfsjkf.SDKJFGSDFLJG