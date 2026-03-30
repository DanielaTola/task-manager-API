import uuid
from .data.database import Base
from sqlalchemy import Column, String

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String(36), primary_key=True, unique=True, index=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String, default="pending")