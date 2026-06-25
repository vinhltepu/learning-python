from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Book Management API", # title cua API , có tác dụng khi truy cập vào tài liệu API
    description="simple API for managing books,authors,categories and book covers", # description cua API ,
    #có tác dụng khi truy cập vào tài liệu API
    version="1.0.0", # version cua API , có tác dụng khi truy cập vào tài liệu API
)

app.mount("/static", StaticFiles(directory="app/static"), name="static") # mount static files for covers images
 # mount thư mục static để phục vụ các tệp tĩnh như hình ảnh bìa sácch
app.include_router(authors.router, prefix="/authors", tags=["Authors"]) 
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])

#static files for covers images


@app.get("/") # định nghĩa một endpoint GET tại đường dẫn gốc ("/") của API. Khi người dùng truy cập vào đường dẫn này, hàm read_root sẽ được gọi.
def read_root():
    return {"message": "Welcome to the Book Management API!"}   
