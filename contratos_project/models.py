from pydantic import BaseModel, EmailStr


class ContratoForm(BaseModel):
    nome: str
    email: EmailStr
    cpf: str
    rg: str
    endereco: str
    pais: str
    valor_contrato: float
