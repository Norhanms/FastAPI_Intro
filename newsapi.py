from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
from enum import Enum
import requests
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
# ----------------------------------------------------
main_url = 'https://newsapi.org/v2/top-headlines?category=general&lang=en&apiKey=b255daf867a940b2bb64d1b6d381580b'
response = requests.get(main_url).json()
print(response)


@app.get('/')
def display():
    return response


'''articles = response["articles"]

templates = Jinja2Templates(directory="templates")


@app.get("/news", response_class=HTMLResponse)
async def read_news(request: Request):
    results = []
    for i in articles:
        results.append(
            {"headline": i["title"], "link": i['url'], 'source': 'newsapi', 'img': i['urlToImage'], 'discription': i["description"]})

    return templates.TemplateResponse("main.html", {"request": request, "res": results})
'''
