python là một ngôn ngữ lập trình bậc cao, được thiết kế để dễ đọc, dễ học và linh hoạt; ra đời năm 1991 và hiện nay rất phổ biến, cú pháp đơn giản gần với ngôn ngữ tự nhiên nên giúp lập trình viên tập trung giải quyết vấn đề hơn là vật lộn với cú pháp phức tạp, đặc biệt khi so sánh với c/c++ thì các lệnh như in chuỗi ra màn hình trong python thường ngắn gọn hơn

tác giả kiểm tra độ phổ biến của python trong năm 2024 bằng stack overflow developer survey, vào mục technology để xem bảng các ngôn ngữ phổ biến; javascript đứng đầu, html và css được nhắc là ngôn ngữ đánh dấu chứ không phải ngôn ngữ lập trình, python nằm trong nhóm top và được tác giả xem là một trong những ngôn ngữ được dùng nhiều; ở mục learning to code thì python được ghi nhận là ngôn ngữ được nhiều người chọn để học nhất trong năm 2024, vì vậy tác giả khuyến khích bắt đầu học với python

lý do python phổ biến gồm: dễ học vì cú pháp đơn giản, đa năng vì dùng được trong nhiều lĩnh vực như phát triển web, khoa học dữ liệu, machine learning/ai, tự động hóa và làm game, và có cộng đồng lớn nên tài liệu phong phú dễ tìm người hỗ trợ; tác giả nêu ví dụ các công cụ phổ biến như django/flask cho web, pandas/numpy/matplotlib cho dữ liệu, tensorflow/scikit-learn cho ai, selenium/beautifulsoup cho tự động hóa và pygame cho game

ide được giải thích là môi trường phát triển tích hợp (công cụ lập trình) như pycharm, vscode, jupyter notebook; tác giả demo viết file .py bằng notepad rồi chạy bằng terminal để thấy bất tiện vì không có số dòng và không có gợi ý code, sau đó mở cùng thư mục bằng vscode để thấy tiện hơn nhờ có số dòng, có thể cài extension để hỗ trợ, và tích hợp terminal ngay trong ide giúp chạy chương trình nhanh và dễ

python được nhấn mạnh là miễn phí, mã nguồn mở, có nhiều thư viện và cộng đồng mạnh nên luôn có tài liệu/diễn đàn hỗ trợ

python là ngôn ngữ thông dịch: mã nguồn được interpreter đọc và thực thi trực tiếp (thường hiểu là chạy ngay khi gọi lệnh), không cần biên dịch thành mã máy trước như các ngôn ngữ biên dịch (ví dụ c/c++/java); demo cho thấy c/c++ phải biên dịch ra file thực thi rồi mới chạy, còn python chỉ cần chạy bằng lệnh python là ra kết quả; ưu điểm là thử nghiệm nhanh và sửa đổi linh hoạt, nhược điểm là hiệu suất thường thấp hơn ngôn ngữ biên dịch, tuy nhiên với nhiều ứng dụng như data/web/automation thì tốc độ phát triển nhanh quan trọng hơn

tác giả làm demo so sánh tốc độ chạy giữa python và c/c++ bằng việc in các số ra terminal, kết quả demo của tác giả cho thấy python có lúc chạy nhanh hơn nên tác giả cũng nói đây chỉ là demo và mỗi ngôn ngữ có ưu nhược riêng

phần cài đặt trên windows: kiểm tra đã có python bằng python --version, nếu chưa thì vào python.org tải bản cho windows, khi cài nhớ tick add python to path, cài xong kiểm tra lại phiên bản và thử tạo file .py rồi chạy để xác nhận hoạt động

cài vscode: tìm “vs code download” tải đúng hệ điều hành, cài xong có thể mở vscode tại thư mục bằng lệnh code ., cài extension python của microsoft để được hỗ trợ tốt hơn; giới thiệu nhanh các khu vực như explorer, search, run and debug, extensions và cách mở terminal trong vscode bằng menu hoặc phím tắt

phần ubuntu: kiểm tra python3, cài bằng sudo apt update rồi sudo apt install python3, chạy file bằng python3; cài vscode có thể qua app center hoặc tải về; nhấn mạnh python đa nền tảng nên cùng một mã có thể chạy trên windows, linux, macos

cách viết python: một là viết trong file .py rồi chạy bằng python/python3, hai là dùng python interactive shell (repl) để gõ lệnh và nhận kết quả ngay; repl là read–eval–print–loop, thoát bằng ctrl+d hoặc exit(); shell chỉ hợp thử nhanh đoạn ngắn, không hợp viết chương trình dài, cuối video tác giả tổng kết đã hướng dẫn cài python, cài ide và cách chạy code