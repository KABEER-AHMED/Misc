from fastapi import FastAPI
from fastapi.responses import JSONResponse
api = FastAPI()

todos = [

    {"id": 1, "task": "Learn FastAPI", "completed": False},
    {"id": 2, "task": "Build an API", "completed": False},
    {"id": 3, "task": "Deploy to production", "completed": False},
    {"id": 4, "task": "create the capstone project", "completed": False},
    {"id": 5, "task": "Use the Project", "completed": False}

]

@api.get("/")
def index():
    return JSONResponse(content={"message": "Hello World!, i am chitti , speed 1 tera hertz, memory 1 zettabyte"})

@api.get("/todos/{id}")
def get_todo(id):
    for todo in todos:
        if todo["id"] == id:
            return JSONResponse(content = todo)