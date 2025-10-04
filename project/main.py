from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}/")  # item_id is a path parameter
async def read_item(item_id: int, query_parameter: int = 11):
    return {"item_id": item_id, "query_parameter": query_parameter}
