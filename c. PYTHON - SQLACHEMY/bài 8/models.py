from sqlalchemy import String , Integer, create_engine, Column
from sqlalchemy.orm import DeclarativeBase, relationship



# bảng user :
# +id  : integer
# +name : string
# +age : integer

# bảng ccds :
# +id : integer
# +so_cccd: string , unique
# +ngay_cap: string
# +noi_cap: string

Base = DeclarativeBase() # class

class User(Base):
    __tablename__ = "users"
    id = Column(name="id", type_=Integer, primary_key=True)
    name = Column(name="user_name", type_=String(50))
    age = Column(name="user_age", type_=Integer)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', age={self.age})"    
    
    CCCD = relationship("CCCD", back_populates="user", uselist=False)

   

    
class CCCD(Base):
    __tablename__ = "cccds"
    id = Column(name="id", type_=Integer, primary_key=True)
    so_cccd = Column(name="so_cccd", type_=String(20), unique=True)
    ngay_cap = Column(name="ngay_cap", type_=String(20))
    noi_cap = Column(name="noi_cap", type_=String(100))

    def __repr__(self) -> str:
        return f"CCCD(id={self.id}, so_cccd='{self.so_cccd}', ngay_cap='{self.ngay_cap}', noi_cap='{self.noi_cap}')"

engine = create_engine("sqlite:///learn_sqlite.db")