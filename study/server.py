from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
import shutil
import os
import ocr
app = FastAPI()
templates = Jinja2Templates(directory="templates")


# @app.get("/")
# def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
def perform_ocr():  # image: UploadFile = File(...)
    # print("post method")
    # temp_file = _save_file_to_disk(image, path="temp", save_as="temp")
    # text = ocr.read_image(temp_file)
    # print(text)
    # return {"filename": image.filename, "text": text}
    return {"hello", "world"}


def _save_file_to_disk(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)
    with open(temp_file, '+wb') as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return temp_file
