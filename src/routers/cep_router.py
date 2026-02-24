from fastapi import APIRouter, HTTPException, Path
from viacep_api.schemas.cep import CepResponse
import requests

router = APIRouter(prefix="/cep", tags=["cep"])

@router.get("/{cep}", response_model=CepResponse)
def get_cep(
    cep: str = Path(..., pattern="^[0-9]{8}$")
):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()

    if "erro" in data:
        raise HTTPException(status_code=404, detail="CEP not found")

    return data