from pythantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Book Management API"

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./app.db"
    
settings = Settings()