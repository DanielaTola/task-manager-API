from enum import Enum
from typing import Optional

from pydantic import BaseModel, field_validator

class TaskStatus(str,Enum): 
    pending = "pending"
    in_progress = "in_progress"
    done = "done"

class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskCreate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None
    priority: TaskPriority | None = None
    
    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v): 
        if v is not None and not v.strip(): 
            raise ValueError("title cannot be empty")
        return v.strip() if v else v


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None
    priority: TaskPriority | None = None
    
    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v): 
        if v is not None and not v.strip(): 
            raise ValueError("title cannot be empty")
        return v.strip() if v else v


class TaskResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: str
    priority: str

    class Config:
        from_attributes = True
