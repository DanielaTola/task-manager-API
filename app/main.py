from fastapi import FastAPI

from .core.database import Base,engine
from .models.task import Task
from .routers.tasks import task_router
from .routers.auth import auth_router

app = FastAPI(title="Task Manager API", version="1.0.0")

app.include_router(task_router)
app.include_router(auth_router)