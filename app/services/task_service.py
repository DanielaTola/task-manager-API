from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from ..models.task import Task
from ..schemas.task import TaskCreate, TaskResponse, TaskUpdate, TaskPriority, TaskStatus


class TaskService:

    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task_create: TaskCreate, owner_id:str) -> TaskResponse:        
        task = Task(
            title=task_create.title.strip(),
            description=task_create.description,
            status=task_create.status,
            priority=task_create.priority,
            owner_id=owner_id
        )

        try:
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, 
                                detail="Failed to create task") from e

        return TaskResponse.from_orm(task)

    def get_task(self, task_id: str, owner_id: str) -> TaskResponse:
        try:
            task = self.db.query(Task).filter(
                Task.id == task_id, 
                Task.owner_id == owner_id).one()
            return TaskResponse.from_orm(task)
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Task not found")

    def get_all_tasks(self, owner_id: str) -> list[TaskResponse]:
        tasks = self.db.query(Task).filter(Task.owner_id == owner_id).all()
        
        return [TaskResponse.from_orm(task) for task in tasks]

    def get_tasks_by_status(self, status: TaskStatus, owner_id: str) -> list[TaskResponse]:
        
        tasks = (
            self.db.query(Task)
            .filter(
                Task.status == status,
                Task.owner_id == owner_id
            )
            .all()    
        )
        
        return [TaskResponse.from_orm(task) for task in tasks]

    def get_task_by_priority(self, priority: TaskPriority, owner_id:str) -> list[TaskResponse]:
        tasks = (
            self.db.query(Task)
            .filter(
                Task.priority == priority, 
                Task.owner_id == owner_id
            )
            .all()
        )
        
        return [TaskResponse.from_orm(task) for task in tasks]
        
        
    def delete_task(self, task_id: str, owner_id: str) -> None:
        try:
            task = self.db.query(Task).filter(
                Task.id == task_id, Task.owner_id == owner_id).one()
            self.db.delete(task)
            self.db.commit()
        except NoResultFound:
            raise HTTPException(status_code=404, 
                                detail="Task not found")
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, 
                                detail="Failed to delete task") from e

    def update_task(self, task_id: str, 
                    task_update: TaskUpdate, 
                    owner_id: str) -> TaskResponse:
        try:
            task = self.db.query(Task).filter(
                Task.id == task_id, 
                Task.owner_id == owner_id).one()
        except NoResultFound:
            raise HTTPException(status_code=404, 
                                detail="Task not found")
        
        task.title = task_update.title.strip()
        if task_update.description is not None:
            task.description = task_update.description.strip() or None
        
        task.status = task_update.status
        task.priority = task_update.priority
        try:
            self.db.commit()
            self.db.refresh(task)
            return TaskResponse.from_orm(task)
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Failed to update task") from e
    
    def complete_task(self, task_id: str, owner_id: str) -> TaskResponse:
        try:
            task = self.db.query(Task).filter(
                Task.id == task_id, 
                Task.owner_id == owner_id).one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Task not found")

        task.status = "done"

        try:
            self.db.commit()
            self.db.refresh(task)
            return TaskResponse.from_orm(task)
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, 
                                detail="Failed to complete task") from e
