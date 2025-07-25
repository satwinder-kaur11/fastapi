# from typing import Union
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/about")
def about():
    return {"hey":"cutie"}

@app.get('/blog/{id}')
def about_item(id):
    return {"data":"id"}


