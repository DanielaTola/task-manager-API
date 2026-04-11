from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from app.core.config import settings


print(f"Using database URL: {settings.database_url}")


def get_engine():
    is_sqlite = settings.database_url.startswith("sqlite")

    connect_args = {"check_same_thread": False} if is_sqlite else {}


    return create_engine (
        settings.database_url, 
        echo=settings.sqlalchemy_echo,
        future = True,
        connect_args=connect_args,
    )

engine = get_engine()

SessionLocal = sessionmaker(
    autocommit = False, 
    autoflush=False,
    bind = engine, 
    future = True,
)

Base = declarative_base()

def get_db() -> Generator [Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()