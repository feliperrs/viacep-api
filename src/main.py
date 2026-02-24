from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

from fastapi import FastAPI
from routers.cep_router import router as cep_router


app = FastAPI()

app.include_router(cep_router)



