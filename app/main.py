from app import models
from fastapi import FastAPI
from .database import engine
from .routers import note, user

models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(note.router)
app.include_router(user.router)



