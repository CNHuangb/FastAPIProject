from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates
from fastapi import Request

import uvicorn

from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM

from api.student import student_api






app = FastAPI()

register_tortoise(
app= app,
config=TORTOISE_ORM
)




app.include_router(student_api,prefix="/student",tags=["选课系统的学生列表"])


# @app.get("/index")
# def index():

#     name = "root"
#     pai = 3.1415926
#     age = 18 
#     books = ["西游记","三国演义","红楼梦","水浒"]

#     return {

#         "index": "index"
#     }

    

if __name__ == '__main__':
    uvicorn.run("main:app", port=8010, reload=True)

