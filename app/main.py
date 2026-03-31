from fastapi import FastAPI

from .data.database import create_tables
from .routers.tasks import task_router

app = FastAPI()
app.include_router(task_router)


@app.on_event("startup")
def on_startup():
    create_tables()
