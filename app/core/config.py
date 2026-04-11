import os 
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

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
    

settings = Settings()

