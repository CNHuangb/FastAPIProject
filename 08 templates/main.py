from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates
from fastapi import Request

import uvicorn


# from jinja2 import Environment, FileSystemLoader, select_autoescape
 
# # 设置模板文件夹路径
# template_dir = 'fastapiproject/08 templates/template2'
# env = Environment(
#     loader=FileSystemLoader(template_dir),
#     autoescape=select_autoescape(['html', 'xml'])
# )

# print("dir")
# print(env.loader.list_templates())


templates = Jinja2Templates(directory="fastapiproject/08 templates/template2")
# # templates = Jinja2Templates(directory="/FastAPIProject/08 templates/temp")




app = FastAPI()



@app.get("/index")
def index(request: Request):

    name = "root"
    pai = 3.1415926
    age = 18 
    books = ["西游记","三国演义","红楼梦","水浒"]

    return templates.TemplateResponse(
           "index.html" ,    
            {
                "request": request,
                "user": name,
                "age": age, 
                "pai" : pai,
                "books": books      

            },
        )

    

if __name__ == '__main__':
    uvicorn.run("main:app", port=8090, reload=True)

