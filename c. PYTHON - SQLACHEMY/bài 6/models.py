from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

"<dialect>+<driver>://<username>:<password>@<host>:<port>/<database_name>"

url = "sqlite:///learn_sqlite.db"  # .db .sqlite .sqlite3

"pymysql"
url_mysql = "mysql+pymysql://root:@127.0.0.1:3306/employee_java"

engine = create_engine(url)

Base = declarative_base()  # class

class Product(Base): 
    __tablename__ = "products"
    id = Column(name="id", type_=Integer, primary_key=True)
    name = Column(name="product_name", type_=String(50))
    price = Column(name="product_price", type_=Float)

Base.metadata.create_all(engine)