from codecs import backslashreplace_errors
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    notes = relationship("Note", back_populates="owner")



class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    note = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="notes")
