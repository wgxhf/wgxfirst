from operator import gt

from click import Path
from fastapi import FastAPI,Path

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World888"}


@app.get("/hello")
async def say_hello():
    return {"message": "nihao"}
@app.get("/lyx/{id}")
async def get_lyx(id: int=Path(...,gt=0,lt=101,description="取值范围1-100")):
    return {"id": id,"title":f"这是第{id} 美美"}

@app.get("/de/{name}")
async def get_name(name: str=Path(...,min_length=3,max_length=100)):
    return {"msg": f"爱情{name}"}

import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

