from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from ..core.database import get_db
from ..schemas.auth import TokenResponse, UserCreate, UserResponse
from ..services.auth_service import AuthService

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/register", 
                response_model=UserResponse, 
                status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, 
             db: Session = Depends(get_db)):
    try:
        return AuthService(db).register_user(user_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)
            )
    
@auth_router.post("/login", 
                response_model=TokenResponse, 
                status_code=status.HTTP_200_OK)
def login(
    login_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)):
    try:
        return AuthService(db).authenticate_user(
            username = login_data.username,
            password = login_data.password
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail=str(e))