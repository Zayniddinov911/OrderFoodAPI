from typing import Union, List

from fastapi import FastAPI
from models import BaseModel, Food, Order

app = FastAPI()

db: List[Order] [
    Order(
        id = ''

    )
]


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/api/v1/orders')
def order_list():
    return db;