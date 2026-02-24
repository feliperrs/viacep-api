from pydantic import BaseModel
from typing import Optional

class CepResponse(BaseModel):
    cep: str
    logradouro: str
    complemento: Optional[str] = None
    unidade: Optional[str] = None
    bairro: str
    localidade: str
    uf: str
    estado: str
    regiao: str
    ibge: str
    gia: str
    ddd: str
    siafi: str