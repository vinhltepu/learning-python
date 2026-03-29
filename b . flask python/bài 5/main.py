from flask import Flask, render_template

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/static/<filename>')
# def static_file(filename):

#     return filename

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)


# 192.168.0.102:3333/static/MVT.png để truy cập vào file MVT.png trong thư mục static

# Client gửi request tới server /<filename>
# Server nhận request và xử lí
# Server sẽ response về phía client