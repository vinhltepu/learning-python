# Bài tập 1: Website giới thiệu bản thân
# Yêu cầu 5 ý
# Tạo route / hiển thị lời chào.
# Tạo route /about giới thiệu ngắn về bản thân.
# Tạo route /contact hiển thị Facebook, số điện thoại, email.
# Tạo route /hobby hiển thị sở thích.
# Tạo route /school hiển thị tên trường hoặc nơi đang học

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Chào mừng đến với website của tôi</h1>'

@app.route('/about')
def about():
    return '<h2>Tôi tên là Vinh. Tôi đang học lập trình Python và Flask.</h2>'

@app.route('/contact')
def contact():
    return 'Facebook: abc <br> SĐT: 0123456789 <br> Email: example@gmail.com'

@app.route('/hobby')
def hobby():
    return 'Sở thích: nghe nhạc, lập trình, đọc sách'

@app.route('/school')
def school():
    return 'Tôi đang học tại ...'

if __name__ == '__main__':
    app.run(debug=True)


# Bài tập 2: Website quán nước mini
# Yêu cầu 5 ý
# Tạo route / hiển thị tên quán.
# Tạo route /menu hiển thị danh sách 3 món nước.
# Tạo route /price hiển thị giá từng món.
# Tạo route /address hiển thị địa chỉ quán.
# Tạo route /open hiển thị giờ mở cửa.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Chào mừng đến với quán nước ABC</h1>'

@app.route('/menu')
def menu():
    return 'Menu: <br> 1. Trà sữa <br> 2. Cà phê <br> 3. Nước cam'

@app.route('/price')
def price():
    return 'Giá: <br> Trà sữa: 25k <br> Cà phê: 20k <br> Nước cam: 30k'

@app.route('/address')
def address():
    return 'Địa chỉ: 123 Nguyễn Văn A, TP.HCM'

@app.route('/open')
def open_time():
    return 'Giờ mở cửa: 7:00 sáng - 10:00 tối'

if __name__ == '__main__':
    app.run(debug=True)



# Bài tập 3: Website tin tức / blog đơn giản
# Yêu cầu 5 ý
# Tạo route / hiển thị trang chủ blog.
# Tạo route /news1 hiển thị tin tức số 1.
# Tạo route /news2 hiển thị tin tức số 2.
# Tạo route /news3 hiển thị tin tức số 3.
# Tạo route /author hiển thị thông tin tác giả

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Trang chủ Blog Flask</h1>'

@app.route('/news1')
def news1():
    return '<h3>Tin 1: Hôm nay tôi bắt đầu học Flask</h3>'

@app.route('/news2')
def news2():
    return '<h3>Tin 2: Flask giúp tạo web bằng Python rất dễ</h3>'

@app.route('/news3')
def news3():
    return '<h3>Tin 3: Tôi đã tạo được nhiều route đầu tiên</h3>'

@app.route('/author')
def author():
    return 'Tác giả: Vinh - Người mới học Flask'

if __name__ == '__main__':
    app.run(debug=True)