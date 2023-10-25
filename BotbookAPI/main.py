from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .SQLPackage import crud, models, schemas
from .SQLPackage.database import SessionLocal

# Command to start API: uvicorn BotbookAPI.main:app --reload

# Initialize API application
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/", response_model=list[schemas.User])
def read_all_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_posts(db, skip=skip, limit=limit)
    return users
    
