from fastapi import APIRouter
from models import *
from typing import List, Union


from fastapi.templating import Jinja2Templates
from fastapi import Request


from pydantic import BaseModel,Field,validator


student_api = APIRouter()

@student_api.get("/")
async def getAllStudent():

    # # 1.查询所有 all方法
    # students = await Studendt.all()    #QuerySet

    # print("students",students)

    # for stu in students:
    #     print (stu.name, stu.sno)

    # print(students[0].name)

    # # 2.过滤查询 filter
    # # students = await Studendt.filter(name="bin")    #QuerySet
    # students = await Studendt.filter(clas_id="1")    #QuerySet
    # print("students",students)

    # for stu in students:
    #     print (stu.name, stu.sno)




    # # 3.过滤查询 get方法：返回模型类对象 
    # stu = await Studendt.get(id="1")    #QuerySet

    # print ("name",stu.name)



    # # 4.模糊查询
    # students = await Studendt.filter(sno__gt="2001")    #QuerySet


    # students = await Studendt.filter(sno__in=["2001","2002"])    #QuerySet
    # students = await Studendt.filter(sno__range=[1,10000])    #QuerySet

    # print (students)



    # # 5.values查询

    # students = await Studendt.filter(sno__range=[1,10000])    #QuerySet
    # students = await Studendt.all().values("name","sno")   #QuerySet

    students = await Studendt.filter(sno__range=[1,10000])    #QuerySet

    print (students)



    return {

        "查看所有的学生":students
    }




@student_api.get("/index.html")
async def getAllStudent(request:Request):

    templates = Jinja2Templates(directory="fastapiproject/09 ORM system/templates")


    students = await Studendt.all()

    return templates.TemplateResponse(
        "index.html",{
            "request":request,
            "students":students
        }
    )
    



class StudentIn(BaseModel):
    name:str
    pwd:str
    sno:int
    clas_id:int
    course:List[int] = []

    
    @validator("name")
    def name_must_alpha(cls,value):
        assert value.isalpha(),"name must be alpha"
        return value
    
    @validator("sno")
    def sno_validate(cls,value):
        assert value>1000 and value<10000,"sno must be range 1000 to 10000"
        return value
    
    


@student_api.post("/")
async def addStudent(student_in:StudentIn):

    # 插入数据到数据库
    # # 方式1

    # student = Studendt(name=student_in.name,pwd=student_in.pwd,sno=student_in.sno,clas_id=student_in.clas_id)
    # await student.save()
    # return {

    #     "操作":"添加一个学生"
    # }


    # 方式2

    student = await Studendt.create(name=student_in.name,pwd=student_in.pwd,sno=student_in.sno,clas_id=student_in.clas_id)
    

    choose_courses = await Course.filter(id__in=student_in.course)
    await student.course.add(*choose_courses)
    # 多对多的关系绑定 

    return student
    


@student_api.get("/{student_id}")
def getOneStudent(student_id:int):

    return {

        "操作":f"查看ID={student_id}的学生"
    }


@student_api.put("/{student_id}")
def updateStudent(student_id:int):

    return {

        "操作":f"更新ID={student_id}的学生"
    }


@student_api.delete("/{student_id}")
def deleteStudent(student_id:int):

    return {

        "操作":f"删除ID={student_id}的学生"
    }
