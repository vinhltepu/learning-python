from fasstapi import APIRouter , Depends , HTTPException , status
from typing import List
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.author import Author , AuthorCreate , AuthorUpdate 
from app import models

router = APIRouter() 
#Truy vấn toàn bộ tác giả trong DB, hỗ trợ phân trang bằng skip và limit
@router.get("/", response_model=List[Author])
def list_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = db.query(models.Author).offset(skip).limit(limit).all()  
    return authors
#Truy vấn chi tiết tác giả theo id , nếu không tìm thấy sẽ trả về lỗi 404
@router.get("/{author_id}", response_model=Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return author
#Tạo mới tác giả, kiểm tra trùng tên trước khi tạo
@router.post("/", response_model=Author)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    existing_author = db.query(models.Author).filter(models.Author.name == author.name).first()
    if existing_author:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Author with this name already exists.")

    author = models.Author(name=author.name, biography=author.biography)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author
#Cập nhật thông tin tác giả, hỗ trợ cập nhật tên và tiểu sử, kiểm tra trùng tên nếu có thay đổi tên
@router.put("/{author_id}", response_model=Author)
def update_author(author_id: int, author_update: AuthorUpdate, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")

    if author_update.name is not None:
        existing_author = db.query(models.Author).filter(models.Author.name == author_update.name).first()
        if existing_author and existing_author.id != author_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Author with this name already exists.")
        author.name = author_update.name

    if author_update.biography is not None:
        author.biography = author_update.biography

    db.commit()
    db.refresh(author)
    return author
#Xóa tác giả theo id, nếu không tìm thấy sẽ trả về lỗi 404, nếu thành công sẽ trả về mã 204 No Content
@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")

    db.delete(author)
    db.commit()