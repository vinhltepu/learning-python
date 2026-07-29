from fastapi import APIRouter, Request

from app.api.deps import templates

router = APIRouter()


@router.get("/admin")
def admin_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="admin/admin.html",
        context={}
    )