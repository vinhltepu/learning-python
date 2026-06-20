from fasstapi import APIRouter , Depends , HTTPException , status
from typing import List
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.category import Category , CategoryCreate , CategoryUpdate 
from app import models

router = APIRouter()    

@router.get("/", response_model=List[Category])
def list_categories(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = db.query(models.Category).offset(skip).limit(limit).all()  
    return categories

@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category

@router.post("/", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    existing_category = db.query(models.Category).filter(models.Category.name == category.name).first()
    if existing_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category with this name already exists.")

    category = models.Category(name=category.name, description=category.description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, category_update: CategoryUpdate, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    if category_update.name is not None:
        existing_category = db.query(models.Category).filter(models.Category.name == category_update.name).first()
        if existing_category and existing_category.id != category_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category with this name already exists.")
        category.name = category_update.name

    if category_update.description is not None:
        category.description = category_update.description

    db.commit()
    db.refresh(category)
    return category