# Khái niệm Python là gì
Python là ngôn ngữ lập trình bậc cao, thiết kế để
 Dễ đọc
 Dễ học
Linh hoạt
Python được phát triển bởi Guido van Rossum, ra đời năm 1991.
Điểm mạnh được nhấn mạnh: cú pháp đơn giản, gần ngôn ngữ tự nhiên, giúp tập trung vào giải quyết vấn đề thay vì cú pháp rườm rà
So sánh nhanh:
  C/C++ khi in ra màn hình thường dài hơn
  Python ngắn gọn hơn (ví dụ print(...))

# Python phổ biến thế nào (dẫn chứng Stack Overflow) (~1:35 → 4:53)
 kiểm tra độ phổ biến bằng Stack Overflow Developer Survey 2024
Trong bảng “Most popular technologies / languages”:
  JavaScript đứng đầu
  HTML/CSS được nói rõ là markup language, không tính là ngôn ngữ lập trình
Python xếp rất cao (tác giả kết luận nếu bỏ HTML/CSS thì Python đứng “rất top”)
Ở mục “Learning to code”
Python được mô tả là ngôn ngữ được yêu thích để học nhiều nhất (tác giả đọc con số 66,4%)
Kết luận phần này: Python được rất nhiều người dùng và chọn để học, nên “tại sao không bắt đầu với Python”

# Lý do Python phổ biến 
Dễ học: cú pháp đơn giản, hợp người mới bắt đầu
Tác giả khuyên: nếu học ngôn ngữ khó hơn trước (C/C++) thì qua Python sẽ rất dễ
Đa năng: dùng web, data science, machine learning/AI, tự động hóa, game
Cộng đồng lớn: nhiều tài liệu, diễn đàn, dễ được giúp khi gặp lỗi
Ví dụ thư viện/framework: Django/Flask, Pandas/NumPy/Matplotlib, TensorFlow/scikit-learn, Selenium/BeautifulSoup, Pygame

# IDE là gì? Demo Notepad vs VS Code
Demo Notepad: tạo demo.py, viết print, chạy bằng terminal “python demo.py”
Nhược điểm Notepad: không số dòng, không gợi ý code, làm việc bất tiện khi code dài
Demo VS Code: mở folder trong VS Code, có số dòng, có extension hỗ trợ, tích hợp terminal
Kết luận: IDE giúp lập trình tiện và nhanh hơn

# Lợi ích của Python 
Miễn phí và mã nguồn mở.
Nhiều thư viện/framework hỗ trợ.
Cộng đồng mạnh, tài liệu phong phú.

# Python thông dịch vs ngôn ngữ biên dịch 
Python là ngôn ngữ thông dịch: chạy qua interpreter, thực thi trực tiếp (dòng theo dòng)
C/C++ là ngôn ngữ biên dịch: phải biên dịch ra file chạy (ví dụ .exe) rồi mới chạy
Demo C++: dùng g++ biên dịch → tạo demo.exe → chạy demo.ex
Demo Python: chạy thẳng “python demo.py”
Ưu điểm Python: thử nghiệm nhanh, sửa xong chạy lại nhanh
Nhược điểm Python: hiệu suất thường thấp hơn C/C++/Java

# Ví dụ hiệu suất Python và C 
Tác giả nói Python thường chậm hơn C/C++/Java, nhưng nhiều lĩnh vực ưu tiên tốc độ phát triển
Demo: in ra terminal từ 0 đến 10.000 ở Python và C++
Kết quả demo của tác giả: Python chạy nhanh hơn (tác giả cũng thấy “ảo”, nói chỉ demo)

# Cài Python trên Windows 
Kiểm tra: mở CMD → “python --version” (ra version là đã cài)
Cài mới: vào python.org → Download → chạy file .exe
Quan trọng: tick “Add python.exe to PATH”
Install Now → cài xong
Test: tạo demo.py, viết print(123), chạy “python demo.py” ra 123
Nếu không thấy đuôi file: View → bật “File name extensions”

# Cài VS Code + extension Python trên Windows 
Tìm “VS Code download” → tải và cài đặt
Có thể mở VS Code bằng terminal: “code .”
Cài extension Python của Microsoft: bấm Install theo gợi ý
Giới thiệu khu vực: Explorer, Search, Run & Debug, Extensions
Mở terminal trong VS Code: Terminal → New Terminal
Phím tắt: Ctrl+Shift+ mở terminal mới; Ctrl+ bật/tắt terminal hiện tại
Có thể đổi theme (color theme/dark mode)

# Cài Python và VS Code trên Ubuntu 
Kiểm tra: “python --version” có thể không có; dùng “python3 --version”
Cài Python: “sudo apt update” → “sudo apt install python3”
Chạy file: “python3 demo.py”
Cài VS Code: tải từ web hoặc vào App Center search “VS Code” rồi Install
Mở folder trong VS Code: kéo thả folder hoặc mở terminal tại folder rồi “code .”

# Viết code Python ở đâu 
Cách 1: viết trong file .py rồi chạy (Windows: python; Ubuntu: python3)
Cách 2: viết trên terminal (Python Interactive Shell/REPL)
REPL: Read (đọc) → Eval (thực thi) → Print (in kết quả) → Loop (lặp)
Ví dụ: gõ “5 + 3” → Enter → ra 8
Thoát: Ctrl+D hoặc “exit()”
Shell chỉ phù hợp đoạn ngắn, không hợp viết chương trình dài