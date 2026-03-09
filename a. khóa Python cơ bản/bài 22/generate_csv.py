import csv
from random import choice, uniform

first_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", 'Đinh', 'Ngô', 'Giang']
middle_names = ['Đức', 'Tuấn', 'Thảo', 'Trà', 'Trọng', 'Gia', 'Bảo']
last_names = ["An", "Bình", "Châu", "Duy", "Khánh", "Minh", 'Linh', 'Nhi', 'Kiệt', 'Đạt', 'Tâm', 'Thành']

point = [(i / 4) for i in range(0,41,1)]

with open('manager_student.csv', 'w', encoding='utf-8', newline='') as file_write:
    csv_write = csv.writer(file_write)
    csv_write.writerow(['Họ và tên', 'Lớp', 'Toán', 'Văn', 'Anh'])
    for _ in range(50):
        full_name = f"{choice(first_names)} {choice(middle_names)} {choice(last_names)}"
        grade = '10D5'
        math = choice(point)
        lect = choice(point)
        en = choice(point)


        csv_write.writerow([full_name, grade, math, lect, en])

## tính toán điểm trung bình 
## nhận xét học sinh xếp loại gfi 
## có được nhận giấy khen không 
  