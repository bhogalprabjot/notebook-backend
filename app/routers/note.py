from typing import List
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from app import models
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.exceptions import RequestValidationError
from .. import schemas, oauth2
from ..database import SessionLocal, engine, get_db
from ..repository import note

router = APIRouter( prefix = "/note", tags=['notes'])


# 1. create note
@router.post("/", response_model = schemas.NoteRes)
async def create_note(request: schemas.Note, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    response.status_code = status.HTTP_201_CREATED
    return note.create(db, request)
    

# 2. read all notes
@router.get("/", response_model = List[schemas.NoteRes])
async def read_note(response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return note.read_all(db)
  

# 3. read note
@router.get("/{id}", response_model = schemas.NoteRes)
async def read_note(id, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    returnedNote = note.read(db, id)
    if returnedNote:
        response.status_code = status.HTTP_200_OK
        return returnedNote
    
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": f"Note with id - {id} doesn't exsist."}


# 4. update note
@router.put("/{id}")
def update_note(id, request: schemas.Note, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    response.status_code = status.HTTP_202_ACCEPTED
    return note.update(db, id, request)

# 5. delete note
@router.delete("/{id}")
def delete_note(id, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    response.status_code = status.HTTP_200_OK
    return note.delete(db, id)

