from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import Response

import uvicorn
import time

app= FastAPI()


@app.middleware("http")
async def m2(request:Request, call_next):
    # 请求代码块    
    print("m2 request")

    response = await call_next(request)

    response.headers["author"] = "yuan"
    # 响应代码块
    print("m2 response")


    return response


@app.middleware("http")
async def m1(request:Request, call_next):
    # 请求代码块    
    print("m1 request")

    # if request.client.host in ["127.0.0.1"] : #黑名单
    #     return Response(status_code=404, content="visit forbidden")
    
    # if request.url.path in ["/user"] : #黑名单
    #     return Response(status_code=404, content="visit forbidden")


    start = time.time()


    response = await call_next(request)


    # 响应代码块
    print("m1 response")

    end = time.time()


    response.headers["Processtimer"] = str(end - start)
    return response
     



@app.get("/user")
def get_user():
    time.sleep(3)

    print("get_user函数执行")
    return {
        "user": "current user"
    }


@app.get("/item/{item id}")
def get_item(item_id: int):

    time.sleep(2)

    print("get_item函数执行")

    return {
        "item id": item_id
    }


if __name__ == '__main__':
    uvicorn.run("main:app",port=8020,reload=True,workers=1)









# app = FastAPI()

# register_tortoise(
# app= app,
# config=TORTOISE_ORM
# )




# app.include_router(student_api,prefix="/student",tags=["选课系统的学生列表"])


# # @app.get("/index")
# # def index():

# #     name = "root"
# #     pai = 3.1415926
# #     age = 18 
# #     books = ["西游记","三国演义","红楼梦","水浒"]

# #     return {

# #         "index": "index"
# #     }

    

# if __name__ == '__main__':
#     uvicorn.run("main:app", port=8010, reload=True)

