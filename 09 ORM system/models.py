from tortoise.models import Model
from tortoise import fields


# 选课系统
# SQL

#例子
# CREATE TABLE Studendt (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(32) NOT NULL COMMENT '姓名',
#     pwd VARCHAR(32) COMMENT '密码',
#     sno INT COMMENT '学号',
#     clas INT,
#     course INT    
# );









class Studendt(Model) :
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32,description="姓名")
    pwd = fields.CharField(max_length=32,description="密码")
    sno = fields.IntField(description="学号")

    clas = fields.ForeignKeyField("models.Clas", related_name="stuedents")

    course = fields.ManyToManyField("models.Course", related_name="stuedents")


# CREATE TABLE Course (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(32) NOT NULL COMMENT '课程名称',
#     # teacher INT
# );


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32,description="课程名称")
    teacher = fields.ForeignKeyField("models.Teacher", related_name="courses")
    addr = fields.CharField(max_length=32,description="教室",default="")


# CREATE TABLE Clas (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(32) NOT NULL COMMENT '班级名称'
# );



class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32,description="班级名称")



# CREATE TABLE Teacher (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(32) NOT NULL COMMENT '老师名称',
#     pwd VARCHAR(32) COMMENT '密码',
#     tno INT COMMENT '老师编号'
# );




class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32,description="老师名称")
    pwd = fields.CharField(max_length=32,description="密码")
    tno = fields.IntField(description="老师编号")