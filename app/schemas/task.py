from typing import Optional

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, Bread, Eggs")
    status: Optional[str] = Field("pending", example="pending")
    priority: Optional[str] = Field("medium", examples="medium")


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, Bread, Eggs")
    status: Optional[str] = Field(None, example="pending")
    priority: Optional[str] = Field("medium", examples="medium")


class TaskResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: str
    priority: str

    class Config:
        from_attributes = True
