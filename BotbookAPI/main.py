from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .SQLPackage import crud, models, schemas
from .SQLPackage.database import SessionLocal

# Command to start API: uvicorn BotbookAPI.main:app --reload

# Initialize API application
app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.get("/posts/", response_model=list[schemas.Post])
def read_all_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_all_posts(db, skip=skip, limit=limit)
    return posts
    
@app.get("/posts/{start_time}/{end_time}", response_model=list[schemas.Post])
def read_posts_between_times(start_time: str, end_time: str,skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts_between_times(db, start_time=start_time, end_time=end_time)
    return posts

@app.get("/comments/{post_id}", response_model=list[schemas.Comment])
def read_all_post_comments(post_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = crud.get_comments_for_post(db, post_id=post_id, skip=skip, limit=limit)
    return comments