from flask import Flask, render_template , request , Response

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ABC123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login-page.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'admin123':
            return render_template('manager-page.html')  # trả về trang quản lý nếu đăng nhập thành công    
        else:
            return 'Login failed'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)