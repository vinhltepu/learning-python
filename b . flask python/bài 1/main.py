from flask import Flask

app = Flask(__name__) # Tạo app Flask. 

# Route
@app.route('/')
def index():
    return '<h1>HELLO WORLD</h1>'

@app.route('/contact')
def contact():
    return 'fb: abc <br> phone number: 0123456789 <br> insta:...'

@app.route('/home')
def home():
    return 'This is home page' 

if __name__ == '__main__':
    app.run(debug=True,host='192.168.0.100') # Chạy Flask ở chế độ debug ;  debug=True giúp:tự động reload khi sửa code.hiện lỗi chi tiết để dễ sửa khi học
# host='127.0.0.1' Server chỉ chạy trên máy của mình, truy cập bằng địa chỉ http://127.0.0.1:5000/ thay bằng địa chỉ mạng của mình 

# if __name__ == '__main__':
#     app.run()

# if __name__ == '__main__': # Kiểm tra file này có đang được chạy trực tiếp hay không 
#     app.run()               

# Endpoint (hay "Điểm cuối") là một thuật ngữ rất phổ biến trong phát triển web, đặc biệt là khi nói về các API (Giao diện lập trình ứng dụng).
# Thuật ngữ "điểm cuối" có thể hiểu theo nghĩa là điểm kết thúc của một quá trình, hoặc nơi mà một yêu cầu (request) từ khách hàng đến ứng dụng được xử lý và trả về phản hồi (response).