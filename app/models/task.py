import uuid

from sqlalchemy import Column, String

from ..core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(
        String(36),
        primary_key=True,
        unique=True,
        index=True,
        default=lambda: str(uuid.uuid4()),
    )
    title = Column(String(255), index=True)
    description = Column(String(255))
    status = Column(String(50),nullable= False,default="pending")
