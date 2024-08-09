from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ResponseBody(BaseModel):
    message: str

@router.get("/hello-Seckin Kintas!")
def prompt() -> ResponseBody:
    return {"message": "Hello, world!"}