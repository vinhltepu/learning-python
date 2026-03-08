with open('manager_student.csv', 'r', encoding='utf-8') as file_read:
    with open('manager_student_copy.csv', 'w', encoding='utf-8') as file_write:
        csv_reader = csv.DictReader(file_read)

        for data in csv_reader:
            # Tính điểm trung bình
            average = round((float(data['Toán']) + float(data['Văn']) + float(data['Anh'])) / 3, 2)


            # Xếp loại hạnh kiểm
            xep_loai = ''

            if average >= 8.0:
                xep_loai = 'Giỏi'
            elif average >= 6.5 and average < 8.0:
                xep_loai = 'Khá'
            else:
                xep_loai = 'Trung bình'

            # Học sinh đó có được giấy khen hay không

            giay_khen = 1 if (xep_loai == 'Giỏi') else 0

            data.update({'Điểm trung bình': average, 'Xếp loại': xep_loai, 'Giấy khen': giay_khen})

            ten_cot = list(data.keys())


            csv_writer = csv.DictWriter(file_write, fieldnames=ten_cot)

            csv_writer.writeheader()

            csv_writer.writerow(data)