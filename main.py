from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

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

@app.post('/apiv3/')
def api3(data: Details):
    return {'message': data}

