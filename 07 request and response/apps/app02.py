from fastapi import APIRouter
from typing import Union

app02 = APIRouter()

@app02.get("/jobs/{kd}")
async def get_jobs(kd, xl:Union[str,None]=None, gj=None):

    return {
        "kd":kd,
        "xl":xl,
        "gj":gj,
    }