from sqlalchemy import String, Integer, create_engine, Column, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class HocSinh(Base):
    __tablename__ = "hoc_sinh"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lop_hoc = relationship("Lop", secondary="hoc_sinh_lop_hoc", back_populates="hoc_sinh")

class Lop(Base):
    __tablename__ = "lop"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    hoc_sinh = relationship("HocSinh", secondary="hoc_sinh_lop_hoc", back_populates="lop_hoc")

class HocSinhLopHoc(Base):
    __tablename__ = "hoc_sinh_lop_hoc"
    id = Column(Integer, primary_key=True)
    hoc_sinh_id = Column(Integer, ForeignKey("hoc_sinh.id"))
    lop_id = Column(Integer, ForeignKey("lop.id"))

engine = create_engine("sqlite:///learn_sqlite.db")
Base.metadata.create_all(engine)




# - hoc sinh :
#   id : integer
#   name : string

# - lop :
#     id : integer
#     name : string

# - hoc_sing_lop_hoc :
#     id : integer
#     hoc_sinh_id : integer
#     lop_id : integer
   