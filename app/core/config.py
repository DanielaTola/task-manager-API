import os 
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent.parent.parent

load_dotenv(BASE_DIR / ".env")

def str_to_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"true", "1", "yes", "on"}

@dataclass(frozen=True)
class Settings: 
    
    app_name: str = os.getenv("APP_NAME", "Task Manager API")
    app_env: str = os.getenv("APP_ENV", "development")
    database_url:str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./task_manager.db",
    )
    sqlalchemy_echo: bool = str_to_bool(os.getenv("SQLALCHEMY_ECHO"), default=False)
    secret_key: str = os.getenv("SECRET_KEY", "change-me")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

settings = Settings()

