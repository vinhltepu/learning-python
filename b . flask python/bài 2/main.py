from flask import Flask , request

#request : gloabl variable => gloabl obiect => request object => Chứa tất cả thông tin về yêu cầu (request) mà client gửi lên server, bao gồm URL, phương thức HTTP, header, body, và các tham số khác.

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return '<h1>HELLO WORLD</h1>'
@app.route('/', methods=['GET', 'POST'])

def index():

    response = make_response()

    response.status_code = 298

    response.content_type = ''

    return response 

@app.route('/product/<product_name>')
def product(product_name):
    return f'PRODUCT NAME IS: {product_name}'

@app.route('/sum/<float:number1>/<float:number2>')
def sum(number1, number2):
    # number1 = int(number1)
    # number2 = int(number2)

    return f'sum of {number1} + {number2} = {number1 + number2}'

@app.route('/file/<path:file_name>')
def file(file_name):
    return f'==> {file_name}'


@app.route('/demo-params')
def demo():
    if 'tien' in request.args:
        money = request.args['tien']

    if 'bimbim' in request.args:
        snack = request.args['bimbim']
    else:
        snack = 'không có gì'

    return f'Giá tiền: là {money} và bimbim là: {snack}' # request.args là một đối tượng chứa tất cả các tham số được truyền qua URL (query parameters). Nó cho phép bạn truy cập và xử lý các tham số này trong ứng dụng Flask của mình.
    
    # money = request.args.get('tien')
    # snack = request.args.get('bimbim', 'không tìm thấy') // ưu tiên sử dụng 
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)


# http://facebook.com:80/contact  => URL
# /contact => route => client nó muốn truy cập vào tài nguyên nào của con server
# facebook.com => domain => 192.168.2.100 (Đây là địa chỉ thật sự => Nhưng mà khó nhớ)


# Dynamic URL là những URL mà các phần trong đó có thể thay đổi hoặc "biến" tùy theo yêu cầu của người dùng. Thay vì chỉ định một đường dẫn cố định, bạn có thể sử dụng dấu <> để chỉ ra các phần động trong URL.

# Các kiểu dữ liệu có thể chấp nhận trong Dynamic URL:
# String (Mặc định):
# 1. Flask mặc định cho phép tất cả các tham số trong URL là kiểu chuỗi (string). Nếu không chỉ định kiểu dữ liệu, Flask sẽ mặc định coi đó là chuỗi.
# 2. Integer: Bạn có thể chỉ định tham số trong URL phải là một số nguyên bằng cách sử dụng kiểu int
# 3. Float: Nếu bạn muốn tham số là một số thực (float), bạn có thể sử dụng kiểu float.
# 4. Path: Để cho phép tham số trong URL có thể chứa nhiều dấu /, bạn có thể dùng kiểu path.
# 5. UUID: Bạn cũng có thể sử dụng UUID để đảm bảo tham số là một định danh duy nhất (thường dùng trong các API).


# Bên trong REQUEST và RESPONSE nó có gì

# - Request và Response đều có 3 phần chính:

# 1. Dòng đầu (Start Line)
# Request: Chứa phương thức (GET, POST,...), đường dẫn (URL) và phiên bản HTTP
# Response: Chứa phiên bản HTTP, mã trạng thái (200, 404,...) và mô tả trạng thái.

# 2. Header (Tiêu đề)
# Chứa các metadata bổ sung như loại nội dung, mã hóa, xác thực,...

# 3. Body (Nội dung, có hoặc không)
# Request: Chứa dữ liệu gửi lên server (thường trong POST, PUT, PATCH).
# Response: Chứa dữ liệu server trả về (JSON, HTML, XML,...).
'''
GET /index HTTP/1.1  //GET: phương thức gửi request , /index: đường dẫn muốn truy cập , HTTP/1.1: phiên bản HTTP
Host: http://192.168.0.102:3333  //địa chỉ server 
User-Agent: (Đây là hệ điều hành và trình duyệt bên phía client) //thông tin về trình duyệt, hệ điều hành bên client 
Accept: text/html // client muốn nhận dữ liệu dạng HTML
'''

'''

Response
HTTP1.1 200 OK  //200 OK nghĩa là request xử lý tốt
Content-Type: text/html //dữ liệu trả về là HTML 
Content-length: 100 (Bytes)  //độ dài của dữ liệu trả về, giúp client biết được khi nào thì nhận đủ dữ liệu
<h1> Hello World </h1> //phần body mà trình duyệt sẽ hiển thị

'''

# GET /quan-jean?tien=1234&bimbim=tony HTTP/1.1

# Tham số trên URL (URL parameters) là các dữ liệu được truyền qua URL trong các yêu cầu HTTP,
# thường là để cung cấp thông tin hoặc xác định các tham số cho trang web hoặc API. Các tham số này
# thường được sử dụng sau dấu ? trong URL và tách nhau bằng dấu &.

# Lưu ý: %3D (dấu =) và %26 (dấu &)


# client => request tới server (method - rất quan trọng) ???
# method nó sẽ giúp server hiểu được mục đích và cách thức xử lí đối với cái request đó.
# Method => ảnh hưởng đến cách dữ liệu được gửi đi
# GET:
# GET /Login?username=tam123&password=tam123 => chỉ dùng để lấy dữ liệu từ phía server

# Có bao nhiêu method???
# Phương thức: GET - Body ❌ Không có - Lấy dữ liệu từ server. Dữ liệu gửi kèm thường nằm trên URL (query parameters).
# Phương thức: POST - Body ✅ Có - Gửi dữ liệu mới lên server (tạo tài nguyên mới).
# Phương thức: PUT - Body ✅ Có - Cập nhật toàn bộ tài nguyên trên server. # account: tam123, password: tam => PUT => account: nhi123 password: nhi
# Phương thức: PATCH - Body ✅ Có - Cập nhật một phần tài nguyên trên server. # account: tam123, password: tam => PATCH => password: tam789
# Phương thức: DELETE - Body ❌ (thường không có) - Yêu cầu xóa tài nguyên trên server.
# Phương thức: HEAD - Body ❌ Không có - Giống GET nhưng chỉ lấy headers, không có body trong response.
# Phương thức: OPTIONS - Body ❌ Không có - Kiểm tra server hỗ trợ những phương thức nào.

# curl: (client url) => công cụ dòng lệnh => để tương tác với server

# windows 10 or 11: có sẵn curl
# linux: có sẵn

# -X: Chỉ định phương thức HTTP (GET, POST, PUT, ...).
# -H: Thêm header vào yêu cầu HTTP.
# -d: Gửi dữ liệu trong body của yêu cầu.
# -I: Yêu cầu HEAD - chỉ lấy headers từ phản hồi của server mà không tải phần body.