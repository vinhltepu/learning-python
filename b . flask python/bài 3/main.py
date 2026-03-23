# Template, Jinja2 và Redirect URL trong Flask 
from flask import Flask, render_template , url_for, redirect

app = Flask(__name__, template_folder='bai 3')

def index(): 
    return ' đây là trang chủ'

# @app.template_global('trangchu')
# def trangchu(n = 2):
#     return f'({n}) Đây là trang chủ'

@app.template_filter('trangchu')
def trangchu(s = str, n=2):
    return s.upper() * n

@app.route('/contact')
def contact():
    return 'Contact Page'

@app.route('/login')
def login():
    return 'Login Page'

@app.route('/home')
def about():
    return 'Home Page'



app.add_template_filter(trangchu, 'trangchu')
@app.route('/', methods=['GET', 'POST'])
def index():
    # tag: i => italic (html => hyper text markup language)
    product_lists = [
        {'name': 'Thắt Lưng Da', 'price': 20000, 'description': 'Sản phẩm dùng thích lắm'},
        {'name': 'Quần Bò', 'price': 500000, 'description': 'Quần làm từ da bò 0'},
        {'name': 'Áo Hoodi', 'price': 150000, 'description': 'Sản phẩm tốt chất lượng cao'}
    ]
    return url_for('contact')

@app.route('/', methods=['GET', 'POST'])
def index():
    # Status code nào về chuyển hướng: 3xx
    # Status code: 302 => chuyển hướng tạm thời
    # Status code: 301 => chuyển hướng vĩnh viễn
    response = make_response('TEST')

    response.status_code = 302

    return response


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # tag: i => italic (html => hyper text markup language)
#     # name = 'Nguyen Van A'
#     # age = 20
#     #return render_template(template_name_or_list='index.html', name='vinh', age=21)

#     return render_template('index.html', trangchu='Đây là trang chủ')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)

# Client: request tới Server
# Server: tiếp nhận request ... => Response tới Client

# Response:
# HTTP/1.1 200 OK
# Content-Type: text/html, charset=utf-8

# body:
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#
# </body>
# </html>



# Template engine: (Công cụ xử lí mẫu)
# => công cụ phần mềm giúp tách biệt Logic xử lí (Chương trình) Và logic hiển thị (Giao diện người dùng)
# => Công cụ tạo các trang web động bằng việc thay thế các phần tử trong mẫu (template). Thao tác với dữ liệu thực tế đc lấy từ server hoặc cơ sở dữ liệu... Phần tử các biến, vòng lặp, hàm,...

# Flask: Jinja2
# Java: Thymleaf
# Javascript: Handlebars
# Nodejs: EJS
# C#: Razor


# Syntax Jinja2: {{ }}, {% %} và {# #}

# {{ }}: Dùng để hiển thị giá trị trong template (biến, phép toán, kết quả hàm).
# {% %}: Dùng để xử lý logic (vòng lặp, điều kiện, kế thừa template, v.v.) mà không in ra giá trị vào HTML.
# {# #}: Dùng để thêm comment vào template, giúp giải thích hoặc ghi chú mà không hiển thị gì trong kết quả HTML.