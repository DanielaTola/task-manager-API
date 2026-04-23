from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..dependencies.auth import get_current_user
from ..models.user import User
from ..schemas.task import TaskCreate, TaskResponse, TaskUpdate
from ..services.task_service import TaskService

task_router = APIRouter(prefix="/tasks", tags=["Tasks"])

@task_router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate, 
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    task_service = TaskService(db=db)
    return task_service.create_task(task_create, current_user.id)

@task_router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: str, 
             db: Session = Depends(get_db),
             current_user: User = Depends(get_current_user)):
    
    task_service = TaskService(db=db)

    return task_service.get_task(task_id, current_user.id)


@task_router.get("/", response_model=list[TaskResponse])
def get_tasks_by_status(status: str | None = None,
                        priority:str | None = None, 
                        db: Session = Depends(get_db),
                        current_user: User = Depends(get_current_user)):
    
    task_service = TaskService(db=db)
    
    if status is not None:
        return task_service.get_tasks_by_status(status, current_user.id)
    
    if priority is not None: 
        return task_service.get_task_by_priority(priority, current_user.id)
    
    return task_service.get_all_tasks(current_user.id)


@task_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
        task_id: str, 
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):
    
    task_service = TaskService(db=db)
    task_service.delete_task(task_id, current_user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@task_router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: str, 
                task_update: TaskUpdate, 
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    task_service = TaskService(db=db)
    return task_service.update_task(task_id, task_update, current_user.id)


@task_router.patch("/{task_id}", response_model=TaskResponse)
def complete_task(task_id: str, 
                  db: Session = Depends(get_db), 
                  current_user: User = Depends(get_current_user)):
    task_service = TaskService(db=db)
    return task_service.complete_task(task_id, current_user.id)