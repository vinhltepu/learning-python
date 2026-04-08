# thực hieenh thao tác crud 
from models import HocSinh, Lop, engine 
from sqlalchemy.orm import Session

with Session(engine) as session:
    # tạo lớp học
    lop1 = Lop(name="Lop 1")
    lop2 = Lop(name="Lop 2")
    session.add_all([lop1, lop2])
    session.commit()
    # tạo học sinh và gán lớp học
    hs1 = HocSinh(name="Nguyen Van A", lop_hoc=[lop1, lop2])
    hs2 = HocSinh(name="Tran Thi B", lop_hoc=[lop1])
    session.add_all([hs1, hs2])
    session.commit()

    # cập nhật tên học sinh
    hs1.name = "Nguyen Van A Updated"
    session.commit()
    # xóa lớp học
    session.delete(lop2)
    session.commit()

    # truy vấn
    hoc_sinh_list = session.query(HocSinh).all()
    for hs in hoc_sinh_list:
        print(hs)
        for lop in hs.lop_hoc:
            print(lop)

  