from .models import Task
from .schemas import TaskCreate, TaskUpdate, TaskResponse
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session 
from fastapi import HTTPException


class TaskService:

    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task_create: TaskCreate) -> TaskResponse:

        if not task_create.title or not task_create.title.strip():
            raise HTTPException(status_code=400, detail="Title is required")
        if task_create.status not in ["pending", "in_progress", "completed"]:
            raise HTTPException(status_code=400, detail="Invalid status value")
        if self.db.query(Task).filter(Task.title == task_create.title).first():
            raise HTTPException(status_code=400, detail="Task with this title already exists")
        
        task = Task(
            title = task_create.title, 
            description = task_create.description, 
            status = task_create.status
        )

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return TaskResponse.from_orm(task)
    
    def get_task(self, task_id: str) -> TaskResponse:
        try:
            task = self.db.query(Task).filter(Task.id == task_id).one()
            return TaskResponse.from_orm(task)
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Task not found")

    def get_all_tasks(self) -> list[TaskResponse]:
        tasks = self.db.query(Task).all()
        return [TaskResponse.from_orm(task) for task in tasks]
    
    def get_tasks_by_status(self, status: str) -> list[TaskResponse]:
        if status not in ["pending", "in_progress", "completed"]:
            raise HTTPException(status_code=400, detail="Invalid status value")
        
        tasks = self.db.query(Task).filter(Task.status == status).all()
        return [TaskResponse.from_orm(task) for task in tasks]  
    
    def delete_task(self, task_id: str) -> None:
        try:
            task = self.db.query(Task).filter(Task.id == task_id).one()
            self.db.delete(task)
            self.db.commit()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Task not found")
        
    def update_task(self, task_id: str, task_update: TaskUpdate) -> TaskResponse:
        try:
            task = self.db.query(Task).filter(Task.id == task_id).one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Task not found")

        if task_update.title is not None:
            task.title = task_update.title
        if task_update.description is not None:
            task.description = task_update.description
        if task_update.status is not None:
            if task_update.status not in ["pending", "in_progress", "completed"]:
                raise HTTPException(status_code=400, detail="Invalid status value")
            task.status = task_update.status

        self.db.commit()
        self.db.refresh(task)

        return TaskResponse.from_orm(task)
    
    def complete_task(self, task_id: str) -> TaskResponse:
        try:
            task = self.db.query(Task).filter(Task.id == task_id).one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Task not found")

        task.status = "completed"
        self.db.commit()
        self.db.refresh(task)

        return TaskResponse.from_orm(task)