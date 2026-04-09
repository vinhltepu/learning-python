from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

"<dialect>+<driver>://<username>:<password>@<host>:<port>/<database_name>"

url = "sqlite:///learn_sqlite.db"  # .db .sqlite .sqlite3

"pymysql"
url_mysql = "mysql+pymysql://root:@127.0.0.1:3306/employee_java"

engine = create_engine(url)

Base = declarative_base()  # class

class User (Base):
    __tablename__ = "users"
    id = Column(name="id", type_=Integer, primary_key=True)
    name = Column(name="user_name", type_=String(50))
    age = Column(name="user_age", type_=Integer)

    def __repr__(self) -> str:     
        return f"User(id={self.id}, name='{self.name}', age={self.age})"
    
class Post(Base):
    __tablename__ = "posts"
    id = Column(name="id", type_=Integer, primary_key=True)
    title = Column(name="post_title", type_=String(100))
    content = Column(name="post_content", type_=String(500))    
  
    def __repr__(self) -> str:
        return f"Post(id={self.id}, title='{self.title}', content='{self.content}', user_id={self.user_id})"