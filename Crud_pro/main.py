# #crud without DB
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional
#
# app = FastAPI()
#
# # temp database
# fakedb = []
#
# # course model to store courses
# class Course(BaseModel):
#     id: int
#     name: str
#     price: float
#     anyfield: Optional[bool] = None
#
# # Home/welcome route
# @app.get("/")
# def read_root():
#     return {"greetings": "Hello zymrians"}
#
# # Get all courses
# @app.get("/courses")
# def get_courses():
#     return fakedb
#
# # get single course
# @app.get("/courses/{course_id}")
# def get_a_course(course_id: int):
#     course = course_id - 1
#     return fakedb[course]
#
# # add a new course
# @app.post("/courses")
# def add_course(course: Course):
#     fakedb.append(course.dict())
#     return fakedb[-1]
#
# # delete a course
# @app.delete("/courses/{course_id}")
# def delete_course(course_id: int):
#     fakedb.pop(course_id-1)
#     return {"task": "deletion successful"}

from fastapi import FastAPI
from schemas.student import Student
from models.students import students,con
app=FastAPI()

@app.get('/')
def home():
    return {
        "type": 'Home page',
        "msg":'helloworld'
    }

# best way to make api
@app.get('/api/students')
async def index():
    data=con.execute(students.select()).fetchall()
    return {
        "success": True,
        "data":data
    }

# insert data
@app.post('/api/students')
def store(student:Student):
    data=con.execute(students.insert().values(
        name=student.name,
        email=student.email,
        age=student.age,
        country=student.country,
    ))

    if data.is_insert:
        return {
            "success": True,
            "msg":"Student Store Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }

# # edit data
# @app.patch('/api/students/{id}')
# async def edit_data(id:int):
#     data=con.execute(students.select().where(students.c.id==id)).fetchall()
#     return {
#         "success": True,
#         "data":data
#     }

# update data

@app.put('/api/students/{id}')
async def update(id:int,student:Student):
    data=con.execute(students.update().values(
        name=student.name,
        email=student.email,
        age=student.age,
        country=student.country,
    ).where(students.c.id==id))
    if data:
        return {
            "success": True,
            "msg":"Student Update Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }

# delete data
@app.delete('/api/students/{id}')
async def delete(id:int):
    data=con.execute(students.delete().where(students.c.id==id))
    if data:
        return {
            "success": True,
            "msg":"Student Delete Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }
