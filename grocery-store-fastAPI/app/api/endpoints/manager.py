from fastapi import APIRouter, Request
from app.api.deps import templates

router = APIRouter()


@router.get("/manager", include_in_schema=False)
def manager_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="manager.html",
        context={}
    )