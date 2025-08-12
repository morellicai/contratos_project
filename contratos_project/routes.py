import os

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# from models import ContratoForm

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, 'templates'))
router = APIRouter()


@router.get('/')
def formulario(request: Request):
    return templates.TemplateResponse('form.html', {'request': request})


# @router.get("/contrato")
