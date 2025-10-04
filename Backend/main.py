from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import service as service

app = FastAPI()

class ChoiceRequest(BaseModel):
    options: List[str]
    winners: int


@app.post("/item")
def registerProcess(request: ChoiceRequest):
    return service.service(request.options,request.winners)