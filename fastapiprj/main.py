from typing import Annotated, Optional
from fastapi import Depends, FastAPI
from pydantic import BaseModel

app = FastAPI()

class STaskAdd(BaseModel):
    name: str
    description: Optional[str]=None

class STask(STaskAdd):
    id: int

tasks = []

@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()],

):
    tasks.append(task)
    
    return {"ok": True}


# @app.get("/tasks")
# async def get_tasks():
#     task = STask(name="Some task")
#     return {"data": task}