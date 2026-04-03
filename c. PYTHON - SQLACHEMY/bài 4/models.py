from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

url = "sqlite:///learn_sqlite.db"
engine = create_engine(url, echo=False)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Float)

Base.metadata.create_all(engine)
