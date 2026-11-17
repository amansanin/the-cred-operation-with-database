from database import create_table,insert_task,get_task,get_task_by_id,update_task,delete_task
from pydantic import BaseModel
from fastapi import FastAPI
create_table()
app= FastAPI()


class TaskCreate(BaseModel):
    title: str
    description: str
    priority:str
    status:str

class TaskUpdate(BaseModel):
    status: str

@app.post("/tasks")
def create_task(task:TaskCreate):

    insert_task(
        task.title,
        task.description,
        task.priority,
        task.status
    )
    return task

@app.get("/tasks")
def read_task():
    tasks=get_task()
    return tasks

@app.get("/tasks/{task_id}")
def read_task_by_id(task_id: int):
    g_t = get_task_by_id(task_id)
    return g_t

@app.put("/tasks/{task_id}")
def update_task_status(task_id:int,task:TaskUpdate):
    update_task(task_id, task.status)
    return{"message":"it is sucessful"}

@app.delete("/tasks/{task_id}")
def delete_task_by_id(task_id:int):
    delete_task(task_id)
    return{"message":"it is delete"}



# from fastapi import FastAPI

# app= FastAPI()

# student=[
#     {"id": 1, "name": "John", "age": 20},
#     {"id": 2, "name": "Alice", "age": 22},
#     {"id": 3, "name": "David", "age": 20} ]
    

# # @app.get("/student")
# # def get_student(age:int=None):
# #     if age is not None:
# #         return[s for s in student if s["age"]== age]
# #     return student


