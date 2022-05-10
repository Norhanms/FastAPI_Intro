from typing import Optional
from fastapi import FastAPI, Request, Query
from pydantic import BaseModel
from enum import Enum
import requests
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return item_id


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"},
                 {"item_name": "Bar"},
                 {"item_name": "Baz"},
                 {"item_name": "Baz"},
                 {"item_name": "Baz"},
                 {"item_name": "Baz"}]


@app.get("/itms/")
async def read_item(q: Optional[str] = Query(None, max_length=50)):
    if q:
        fake_items_db.append(q)
    return fake_items_db
