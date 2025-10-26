from fastapi import FastAPI, Query, Header, Response
from typing import Annotated, Union
from pydantic import BaseModel
import asyncio

app = FastAPI()
# items = ["Tシャツ", "スカート", "ブーツ", "コート"]

# @app.get("/") 
# @app.get("/sample") 
# def read_root():
#   return {"message": "APIです"}

# @app.get("/items/sample") 
# def read_item():
#   return {"message": "APIです"}

# @app.get("/items/{item_id}") 
# def read_item(item_id):
#   return {"item_id": item_id, "item_name": "Tシャツ"}

# @app.get("/items/{item_id}/detail") 
# def read_item(item_id):
#   return {"item_id": item_id, "item_name": "Tシャツ"}


"""
ge -> 以上
le -> 以下
gt -> より大きい(指定した値を含まない)
lt -> より小さい(指定した値を含まない)
"""

# @app.get("/items") 
# def read_item(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)] = 10):
#   return {"items": items[skip: skip + limit]}


# class Item(BaseModel):
#   name: str
#   price: float
#   description: Union[str, None] = None

# @app.post("/items/")
# def create_item(item: Item):
#   print(f"データを登録します: {item.name}, {item.price}, {item.description}")
#   return item
  
# @app.get("/sample/")
# def read_sample(response: Response ,authorization: Union[str, None] = Header(default=None)):
#   print(authorization)
#   response.headers["custom-header"] = "12345"
#   return {"message": "ヘッダー情報を取得しました"}

@app.get("/sleep_time/")
async def sleep_time(sec: int):
  await asyncio.sleep(sec)
  return {"message": f"{sec}秒"}