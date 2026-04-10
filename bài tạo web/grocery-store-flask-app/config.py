import os
# cấu hình cho ứng dụng Flask
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key' # nên thay đổi trong môi trường sản xuất
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///quangthuy_store.db' # sử dụng SQLite cho phát triển, có thể thay đổi sang PostgreSQL hoặc MySQL trong sản xuất
    SQLALCHEMY_TRACK_MODIFICATIONS = False # tắt tính năng theo dõi thay đổi để tiết kiệm tài nguyên            