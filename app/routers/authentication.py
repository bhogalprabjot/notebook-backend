from app import models, token
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from .. import schemas, database, models, hashing, token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags = ["login"])

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not hashing.Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password")

    # geenerate JWT token
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}


