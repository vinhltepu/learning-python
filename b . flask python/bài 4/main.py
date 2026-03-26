# Bài 4: Thẻ Form, Request và Response trong Flask Web Development

from urllib import request

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    username = ''
    password = ''
    if 'username' in request.args and 'password' in request.args:  # Kiểm tra nếu có dữ liệu username và password trong request
        username = request.form.get('username')  # Lấy giá trị username từ form
        password = request.form.get('password')  # Lấy giá trị password từ form
        print(f'Username: {username}, Password: {password}')  # In ra console
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)