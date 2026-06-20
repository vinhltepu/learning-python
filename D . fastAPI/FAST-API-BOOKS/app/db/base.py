from sqlalchemy.orm import declarative_base 

Base = declarative_base()

# import models to register them with SQLAlchemy's metadata
from app.models.author import Author
from app.models.book import Book
from app.models.category import Category

