from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.schemas.auth import TokenResponse, UserCreate, UserLogin


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_data: UserCreate) -> User:

        #Validate password strength
        self._validate_password_strength(user_data.password)
        #Validate unique username and email
        self._validate_unique_fields(user_data)
        
        user = User(
            name = user_data.name,
            last_name = user_data.last_name,
            date_of_birth = user_data.date_of_birth,
            username = user_data.username,
            email = user_data.email,
            hashed_password = hash_password(user_data.password)
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def _validate_password_strength(self, password: str) ->None:
        """Implement password strength validation logic here, 
        such as checking for minimum length, 
        presence of uppercase letters, 
        numbers, and special characters."""
        if len (password) < 8: 
            raise ValueError("Password must be at least 8 characters long")
        if not any(c.isupper() for c in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in password):
            raise ValueError("Password must contain at least one number")
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in password):
            raise ValueError("Password must contain at least one special character")
    
    def _validate_unique_fields(self, user_data:UserCreate) ->None:
        """Check if the username and email are unique in the database."""
        existing_user = self.db.query(User).filter(
            or_(User.username == user_data.username, User.email == user_data.email)
        ).first()

        if existing_user:
            if existing_user.username == user_data.username:
                raise ValueError("Username already exists")
            if existing_user.email == user_data.email:
                raise ValueError("Email already exists")

    def authenticate_user(self, login_data: UserLogin) -> TokenResponse:

        user = self.db.query(User).filter(User.username == login_data.username).first()
        if not user or not verify_password(login_data.password, user.hashed_password):
            raise ValueError("Invalid username or password")

        access_token = create_access_token(data={"sub": user.id, "email": user.email})

        return TokenResponse(access_token=access_token, token_type="bearer")   
