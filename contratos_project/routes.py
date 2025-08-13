from http import HTTPStatus
import os
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr
from contratos_project.models import ContratoForm

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, 'templates'))

router = APIRouter()


@router.get('/forms', status_code=HTTPStatus.OK)
def formulario(request: Request):
    return templates.TemplateResponse('form.html', {'request': request})


@router.post(
    '/contrato', status_code=HTTPStatus.OK, response_model=ContratoForm
)
def geraContrato(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    contato: str = Form(...),
    cpf: str = Form(...),
    rg: str = Form(...),
    endereco: str = Form(...),
    item: str = Form(...),
    valor_contrato: float = Form(...),
):
    contrato_data = ContratoForm(
        nome=nome,
        email=email,
        contato=contato,
        cpf=cpf,
        rg=rg,
        endereco=endereco,
        item=item,
        valor_contrato=valor_contrato,
    )

    return templates.TemplateResponse(
        'contrato.html', {'request': request, **contrato_data.model_dump()}
    )
