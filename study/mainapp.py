from typing import Optional
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/name")
def fullname(fname: str, lname: str):
    name = fname.title() + lname.title()
    return {"name": name}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


def info(name: str, age: int):
    return age + name
