import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session 
from typing import Generator


SQLITE_FILE_NAME = os.getenv("DATABASE_FILE", "tasks_manager.db")
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SQLITE_URL = f"sqlite:///{os.path.join(BASE_DIR, SQLITE_FILE_NAME)}"

ECHO = os.getenv("SQLALCHEMY_ECHO", "False").lower() == "true"


engine = create_engine(
    SQLITE_URL, 
    echo=ECHO,
    connect_args={"check_same_thread": False} 
)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)   