from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel,Field,validator
from datetime import date
from typing import List

from fastapi import Request

import os

app06 = APIRouter()

@app06.post("/items")
async def items(request: Request):

    print("URL:",request.url)
    print("客户端IP地址:",request.client.host)
    print("客户端宿主信息:",request.headers.get("user-agent"))
    print("cookies:",request.cookies)

    return {
        "URL:":request.url,
        "客户端IP地址:":request.client.host,
        "客户端宿主信息:":request.headers.get("user-agent"),
        "cookies:":request.cookies,
    }



