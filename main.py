from typing import Optional,Annotated
from fastapi import FastAPI,Form
from pydantic import BaseModel
import os
from mistralai import Mistral


class Details(BaseModel):
    f_name: str
    l_name: str
    phone_number: int

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
    
@app.get('/apiv1/{name}')
def api1(name: str):
    return {'message': f'Hello! @{name}'}


@app.get('/apiv2/')
def api2(name: str):
    return {'message': f'Hello! @{name}'}



@app.get('/cv/')
def cv(name: str):
    api_key= os.environ.get('MISTRAL_API_KEY')
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "résume les compétences en intelligence artificielle"
                },
                {
                    "type": "document_url",
                    "document_url": "https://fastapi-3qc2.onrender.com/moncv.pdf"
                }
            ]
        }
    ]
    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )
    return {chat_response}

@app.post('/apiv3/')
def api3(data: Details):
    return {'message': data}

@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


class ModelInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(data: ModelInput):
    # Exemple simple de "prédiction"
    score = (data.sepal_length + data.sepal_width + data.petal_length + data.petal_width) / 4
    return {"prediction": score}

