"""Starter Code: FastAPI REST APIs"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST APIs")


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


TASKS = [
    Task(id=1, title="Set up FastAPI project", completed=True),
    Task(id=2, title="Create API routes"),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST APIs assignment!"}


@app.get("/tasks")
def list_tasks(only_completed: bool = False):
    tasks = TASKS
    if only_completed:
        tasks = [task for task in TASKS if task.completed]
    return {"tasks": tasks}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in TASKS:
        if task.id == task_id:
            return task
    return {"detail": "Task not found"}


@app.post("/tasks")
def create_task(task: Task):
    return {"message": "Task received", "task": task}
