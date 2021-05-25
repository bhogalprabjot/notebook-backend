from pydantic import BaseModel
from typing import List
#TODO: 1. Create a proper schema for Note
"""
title
note
date and time of creation
date and time of update
password protected


"""

class Note(BaseModel):
    title: str
    note: str

# this is the schema for response
class NoteRes(BaseModel):
    title: str
    note: str
    owner_id: int
    # owner: UserRes

    class Config():
        orm_mode=True


# User class
class User(BaseModel):
    name: str
    email: str
    password: str

# User response
class UserRes(BaseModel):
    name: str
    email: str
    notes: List[NoteRes] = []

    class Config():
        orm_mode = True

