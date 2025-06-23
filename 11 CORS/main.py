from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import Response

from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import time

app= FastAPI()



 
# 配置CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的源，可以替换为特定域名，例如 ["http://localhost:8080"]
    allow_credentials=True,
    allow_methods=["*"],  # 允许的请求方法（GET, POST, PUT, DELETE等）
    allow_headers=["*"],  # 允许的请求头
)







# @app.middleware("http")
# async def myCORSMiddleware(request:Request, call_next):
    
#     response = await call_next(request)

#     response.headers["Access-Control-Allow-Origin"] = "*"
#     return response
     
    
     



@app.get("/user")
def get_user():


    print("get_user函数执行","bin")
    return {
        "user": "bin"
    }




if __name__ == '__main__':
    uvicorn.run("main:app",port=8030,reload=True,workers=1)








