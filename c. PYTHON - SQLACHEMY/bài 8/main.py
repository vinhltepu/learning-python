from models import CCCD , User, engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    # tạo user 
    user1 = User(name="A", age=30)
    user2 = User(name="B", age=25)    
    # lưu user vào db
    session.add_all([user1, user2]) 
    session.commit()
    # tạo cccd
    cccd1 = CCCD(so_cccd="123456789", ngay_cap="2020-01-01", noi_cap="Hanoi", user=user1)
    cccd2 = CCCD(so_cccd="987654321", ngay_cap="2021-02-01", noi_cap="HCM", user=user2)
    session.add_all([cccd1, cccd2])
    session.commit()
    # cập nhật 
    user1.name = "A Nguyen"
    print(user1)
    session.commit()
    # xóa cccd
    session.delete(cccd2)
    session.commit()
    # truy vấn
    users = session.query(User).all()
    for user in users:
        print(user)
        print(user.CCCD)    