from fastapi import FastAPI

from .core.database import Base, engine
from .routers.auth import auth_router
from .routers.tasks import task_router

app = FastAPI(title="Task Manager API", version="1.0.0")

app.include_router(task_router)
app.include_router(auth_router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(
        bind=engine
    )
