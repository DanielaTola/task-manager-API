from fastapi import FastAPI
from .crud import task_router
from .data.database import create_tables

app = FastAPI()
app.include_router(task_router)

@app.on_event("startup")
def on_startup():
    create_tables()
