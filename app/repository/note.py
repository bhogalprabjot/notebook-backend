from typing import List
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from app import models
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.exceptions import RequestValidationError
from .. import schemas
from ..database import SessionLocal, engine, get_db

# create note in database
def create(db: Session, request: schemas.Note):
    new_note = models.Note(title = request.title, note = request.note, owner_id = 1)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

# get all  notes form database
def read_all(db: Session):
    return db.query(models.Note).all()
   
# get a single note with id from database
def read(db: Session, id: int):
    return db.query(models.Note).filter(models.Note.id == id).first()

# update note in database
def update(db:Session, id: int, request: schemas.Note):
    updated_note = db.query(models.Note).filter(models.Note.id == id)
    if not updated_note:
        raise HTTPException(status_code=404, detail=f"Cannot find note with id {id}")
    updated_note.update({"title": request.title, "note": request.note})
    db.commit()
    return "updated"

def delete(db:Session, id: int):
    note = db.query(models.Note).filter(models.Note.id == id)
    if not note.first():
        raise HTTPException(status_code=404, detail=f"Cannot find note with id {id}")
    note.delete(synchronize_session=False)
    db.commit()
    return "Deleted"