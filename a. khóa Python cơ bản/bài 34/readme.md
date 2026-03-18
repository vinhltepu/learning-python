# Biến __name__ trong Python 

# biến __name__ là một biến đặc biệt được sử dụng để xác định xem mã nguồn của một file đang được chạy trực tiếp hayimport vào một module khác. Điều này rất quan trọng khi bạn muốn phân biệt hành vi của một chương trình khi nó đượcthi trực tiếp so với khi nó được sử dụng như một phần của chương trình khác.

if __name__ == '__main__':
    print(__name__)
    print('demo')