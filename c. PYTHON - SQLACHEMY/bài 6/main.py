from models import engine, Product
from sqlalchemy.orm import Session

# in_ : dùng để kiểm tra các giá trị có thuộc một danh sách các giá trị hay không
# is_ : dùng để kiểm tra xem một giá trị có phải là None hay không
# like : so sánh chuỗi phân biệt chữ hoa chữ thường
# ilike : so sánh chuỗi không phân biệt chữ hoa chữ thường
# pattern :
# + % : đại diện cho bất kỳ chuỗi nào (bao gồm cả chuỗi rỗng)
# + _ : đại diện cho một ký tự bất kỳ

session = Session(bind=engine)


if not session.query(Product).first():
    session.add_all([
        Product(name='Laptop', price=1500.0),
        Product(name='Smartphone', price=1200.0),
        Product(name='Tablet', price=900.0),
        Product(name='Laptop', price=1700.0),
    ])
    session.commit()

print('Bảng sản phẩm giống bài 5:')
print('ID\tTên sản phẩm\tGiá')
for p in session.query(Product).order_by(Product.id):
    print(f"{p.id}\t{p.name}\t{p.price}")

result = session.query(Product).filter(Product.name.in_(['Laptop', 'Smartphone'])).all()  # truy vấn sản phẩm có tên Laptop hoặc Smartphone
query = session.query(Product).filter(Product.name.is_(None)).all()  # truy vấn sản phẩm có tên None
like_query = session.query(Product).filter(Product.name.like('%Laptop%')).all()  # truy vấn tên chứa Laptop
ilike_query = session.query(Product).filter(Product.name.ilike('%laptop%')).all()  # truy vấn tên chứa laptop, không phân biệt hoa/thường

print('\nKết quả truy vấn:')
print('Laptop/Smartphone:', result)
print('Tên None:', query)
print('Tên chứa Laptop:', like_query)
print('Tên chứa laptop (ilike):', ilike_query)

session.close()