from typing import List
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from app import models
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.exceptions import RequestValidationError
from .. import schemas
from ..database import SessionLocal, engine, get_db
from ..hashing import Hash
from ..repository import user

router = APIRouter(prefix = "/user", tags=['user'])

# 1. Create User
@router.post("/", response_model = schemas.UserRes)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
   return user.create(db, request)

# 2. Get User
@router.get("/{id}", response_model = schemas.UserRes)
def get_user(id, response: Response, db: Session = Depends(get_db)):
    response.status_code = status.HTTP_200_OK
    return user.read(db, id)