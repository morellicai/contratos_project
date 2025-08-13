from pydantic import BaseModel, EmailStr


class ContratoForm(BaseModel):
    nome: str
    email: EmailStr
    contato: str
    cpf: str
    rg: str
    endereco: str
    item: str
    valor_contrato: float
