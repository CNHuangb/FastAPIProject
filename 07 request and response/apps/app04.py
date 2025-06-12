from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel,Field,validator
from datetime import date
from typing import List

from fastapi import Form

app04 = APIRouter()

@app04.post("/regin")
async def reg(username:str = Form(),password: str = Form()):

    print(f"username: {username}, password:{password} ")
    return {

        "username":username
    }