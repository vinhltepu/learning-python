# Bài 4: Thẻ Form, Request và Response trong Flask Web Development

from urllib import request

from flask import Flask, render_template

app = Flask(__name__)

USERNAME = 'admin'
PASSWORD = 'admin123'



# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('index.html')
    
    # elif request.method == 'POST':  
    #     username = request.form.get('username')  # lấy dữ liệu từ form gửi lên server
    #     password = request.form.get('password')  # lấy dữ liệu từ form gửi lên server
        
    #     if username == USERNAME and password == PASSWORD:
    #         return 'admin login success'
    #     else:
    #         return render_template('login.html', error='Invalid username or password')




# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')

#     if username == USERNAME and password == PASSWORD:
#         return 'Chúc mừng admin đã đăng nhập thành công'
#     else:
#         return render_template('login.html')


# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')

#     avatar = request.files.get('file')

#     avatar.save('avatar_server.png')

#     if username == USERNAME and password == PASSWORD:
#         return f'Chúc mừng admin đã đăng nhập thành công với avatar là: {avatar.filename}.'
#     else:
#         return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    list_file = request.files.getlist('file')

    file_names = [f.filename for f in list_file]

    for f in list_file:
        f.save(f.filename)

    if username == USERNAME and password == PASSWORD:
        return f'Chúc mừng admin đã đăng nhập thành công với danh sách các file là: {file_names}.'
    else:
        return render_template('login.html')


@app.route('/handle-pdf')
def handle():

    with open('dethi-lop9.pdf', 'rb') as file:
        content_pdf = file.read()

    response = Response(content_pdf, content_type='application/pdf')

    response.headers['Content-Disposition'] = 'attachment; filename="dethi-lop9.pdf"'   
    return response

# Response:
# Header:
# content-type: application/pdf
# content-disposition: inline; filename="server-pdf.pdf

# body:
# 101010101001


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)