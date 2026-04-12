from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel): 
    name: str = Field(..., example="John Doe")
    last_name: str = Field(..., example="Doe")
    date_of_birth: Optional[datetime] = Field(None, example="1990-01-01")
    username: str = Field(..., example="johndoe")
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="strongpassword123")

class UserResponse(BaseModel):
    id: str
    name: str
    last_name: str
    date_of_birth: Optional[datetime]
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True    
class UserLogin(BaseModel):
    username: str = Field(..., example="johndoe")
    password: str = Field(..., example="strongpassword123")


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"