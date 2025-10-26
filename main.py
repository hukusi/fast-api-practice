from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()
items = ["Tシャツ", "スカート", "ブーツ", "コート"]

# @app.get("/") 
@app.get("/sample") 
def read_root():
  return {"message": "APIです"}

@app.get("/items/sample") 
def read_item():
  return {"message": "APIです"}

@app.get("/items/{item_id}") 
def read_item(item_id):
  return {"item_id": item_id, "item_name": "Tシャツ"}

@app.get("/items/{item_id}/detail") 
def read_item(item_id):
  return {"item_id": item_id, "item_name": "Tシャツ"}


"""
ge -> 以上
le -> 以下
gt -> より大きい(指定した値を含まない)
lt -> より小さい(指定した値を含まない)
"""

@app.get("/items") 
def read_item(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)] = 10):
  return {"items": items[skip: skip + limit]}

