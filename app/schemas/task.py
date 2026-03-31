from typing import Optional

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, Bread, Eggs")
    status: Optional[str] = Field("pending", example="pending")


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, Bread, Eggs")
    status: Optional[str] = Field(None, example="pending")


class TaskResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: str

    class Config:
        from_attributes = True
