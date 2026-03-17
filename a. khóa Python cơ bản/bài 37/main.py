## Phân Biệt Module, Package và Library trong Python 
# Module  là file .py chứa code Python (hàm, class, biến)
# Package là thư mục chứa nhiều module, có file __init__.py
# Library là tập hợp các module và package để cung cấp tính năng mạnh mẽ
# Muốn tắt cái tự động tạo folder __pycache__ thì các vào cái biến môi trường
# tạo cái biến này
# PYTHONDONTWRITEBYTECODE 1
# Từ Python 3.3 trở đi, file __init__.py không còn bắt buộc để tạo package nữa

from demo import count_number

from demo import greeting

count_number()

greeting()