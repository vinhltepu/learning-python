from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.api.deps import get_db, templates
from app import models

router = APIRouter()


@router.get("/", include_in_schema=False)
def shop_page(
    request: Request,
    db: Session = Depends(get_db)
):

    products = db.query(models.Product).all()

    return templates.TemplateResponse(
        request=request,
        name="dashboard/shop.html",
        context={
            "products": products
        }
    )