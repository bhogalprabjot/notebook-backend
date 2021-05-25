"""
currently using SQLite
later use PostGreSQL or MySQL
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#url to database
SQLALCHEMY_DATABASE_URL = "sqlite:///./noteSQLite.db"

#creates theh database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# session objec
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
