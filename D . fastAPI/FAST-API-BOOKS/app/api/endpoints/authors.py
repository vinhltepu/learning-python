from fastapi import APIRouter

router = APIRouter() # tạo một đối tượng APIRouter để định nghĩa các endpoint liên quan đến tác giả (authors).
@router.get("/") # dùng phương thức Get để lấy danh sách các tác giả. 
def list_authors():
    return {"message": "List-authors do it later"}