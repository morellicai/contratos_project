from fastapi import APIRouter, Request, Form
# from fastapi.response import RedirectResponse
from fastapi.templating import Jinja2Templates
from models import ContratoForm

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/")
def formulario(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# @router.get("/contrato")
