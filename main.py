from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get('/apiv1/{name}')
def api1(name: str):
    return {'message': f'Hello! @{name}'}


@app.get('/apiv2/')
def api2(name: str):
    return {'message': f'Hello! @{name}'}

@app.post('/apiv3/')
def api3(data: Details):
    return {'message': data}
