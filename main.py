from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory storage
tasks = []
task_id_counter = 1


class Task(BaseModel):
    title: str
    completed: bool = False


@app.get("/")
def read_root():
    return {"message": "Welcome to TaskFlow API"}


@app.get("/health")
def health_check():
    return {"status": "Application is running"}


@app.post("/tasks")
def create_task(task: Task):
    global task_id_counter

    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)
    task_id_counter += 1

    return new_task
