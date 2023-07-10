from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn #--->To change the port number we can use uvicorn for debuging process 

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


app = FastAPI()


@app.get("/hello")
def get():
    return {"Hello": "World"}


@app.get("/all")
def all():
    return {"data": {"name": "prsanna"}}


@app.get("/about")
def about():
    return {"data": "about page"}


@app.get("/")
def blog():
    return {"data":"blog"}


@app.get("/blog/{id}")
def show(id:int):
    return {"data": id}


@app.get("/check")
def check_optional_name(name: Optional[str]="user"):
    return {"message":f"Hello {name}"}


# Limit and published both are in query parameter 
@app.get("/lap")
# We have to assign the value fro limit and published if we are not asssigning
# -- in the browser it will shows error so we have to assign the default value
def lap(limit = 10, published :bool = True, sort: Optional[str] = None):    
    if published:
        return {"data":f"{limit} Published is True"}
    else:
        return {"Data":f"{limit} Published is False"}
    # http://127.0.0.1:8000/lap?limit=100&published=false


@app.post("/blog")
def create(blog: Blog):
    return {"data":f"Blog created with the title as {blog.title}"}



# If i want to use the diff port number
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)

