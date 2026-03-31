from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import Response
from ..data.database import get_db
from ..schemas.task import TaskCreate, TaskUpdate, TaskResponse
from ..services.task_service import TaskService


task_router = APIRouter(prefix="/tasks", tags=["Tasks"])

@task_router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate, db:Session = Depends(get_db)):
    task_service = TaskService(db=db)
    return task_service.create_task(task_create)

@task_router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: str,db:Session = Depends(get_db)):
    task_service = TaskService(db=db)

    return task_service.get_task(task_id)

@task_router.get("/", response_model=list[TaskResponse])
def get_tasks_by_status(status: str | None = None, db:Session = Depends(get_db)):
    task_service = TaskService(db=db)
    if status is not None: 
        return task_service.get_tasks_by_status(status)
    return task_service.get_all_tasks()

@task_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, db:Session = Depends(get_db)):
    task_service = TaskService(db=db)
    task_service.delete_task(task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@task_router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: str, task_update: TaskUpdate, db:Session = Depends(get_db)):
    task_service = TaskService(db=db)
    return task_service.update_task(task_id, task_update)

@task_router.patch("/{task_id}", response_model=TaskResponse)
def complete_task(task_id: str, task_update: TaskUpdate, db:Session = Depends(get_db)):
    task_service = TaskService(db=db)
    return task_service.complete_task(task_id)
