from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    c: float
    d: float

@app.post("/restar")
def restar(valores: Input):
    return {"resultado": valores.c - valores.d}
