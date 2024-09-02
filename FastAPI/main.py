from typing import Union

from fastapi import FastAPI, HTTPException, Depends, Response, status, Request

import json

from typing import Annotated

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from fastapi.templating import Jinja2Templates

app = FastAPI()

origins = ['http://localhost:3000']
# A port for different app, where it is allowed to call our fastAPI app only if it is running on localhost:3000

app.add_middleware(CORSMiddleware, allow_origins=origins)

templates = Jinja2Templates(directory="templates")

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# my_items = [
#     {
#         "item_id": 1,
#         "name": "Potatoes",
#         "price": 40
#     },
#     {
#         "item_id": 2,
#         "name": "Tomatoes",
#         "price": 50
#     }
# ]

class KPIS(BaseModel):
    DOMAIN: str
    INDUSTRY: str
    SECTOR: str
    CLASSIFICATION: str
    DEPARTMENT: str
    SUBDEPARTMENT: str
    KPIS: str
    EXPLANATION: str
    FORMULA: str
    DeptID: int

fileloc = r'C:\\Users\\ShashankMauli\\Documents\\GitHub\\fastapi-react-app\\FastAPI\\segregated_kpis\\'
filename = "ProductDevelopment+ResearchandDevelopment+ConceptDevelopment.json"
json_file = fileloc + filename
with open(json_file, 'r', encoding='utf-8') as infile:
    data = json.load(infile)

print (data)


# def find_items(id):
#     for i in my_items:
#         if i['item_id'] == id:
#             return i


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
    # return {"Hello": "World"}


# @app.get("/items")
# async def get_items():
#     return {"data": my_items}


fileloc = r'C:\\Users\\ShashankMauli\\Documents\\GitHub\\fastapi-react-app\\FastAPI\\repository\\'
filename = "nested_json_structure.json"
json_file = fileloc + filename
with open(json_file, 'r', encoding='utf-8') as infile:
    data = json.load(infile)


@app.get("/kpis")
async def get_items():
    return data


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
