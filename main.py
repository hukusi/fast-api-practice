from fastapi import FastAPI

app = FastAPI()

# @app.get("/") 
@app.get("/sample") 
def read_root():
  return {"message": "APIです"}

@app.get("/items/sample") 
def read_root():
  return {"message": "APIです"}

@app.get("/items/{item_id}") 
def read_item(item_id):
  return {"item_id": item_id, "item_name": "Tシャツ"}

@app.get("/items/{item_id}/detail") 
def read_item(item_id):
  return {"item_id": item_id, "item_name": "Tシャツ"}