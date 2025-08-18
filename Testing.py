from fastapi import FastAPI
from fastapi.responses import JSONResponse
api = FastAPI()

@api.get("/")
def index():
    return JSONResponse(content={"message": "Hello World!, i am chitti , speed 1 tera hertz, memory 1 zettabyte"})
    return {"message": "Hello World!, i am chitti , speed 1 tera hertx, memory 1 zettabyte"}
