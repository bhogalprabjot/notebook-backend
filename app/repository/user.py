from typing import List
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from app import models
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.exceptions import RequestValidationError
from .. import schemas
from ..database import SessionLocal, engine, get_db
from ..hashing import Hash


def create(db: Session, request: schemas.User):
    new_user = models.User(name = request.name, email = request.email, password = Hash.encrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def read(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id - {id} not found!")
    return user