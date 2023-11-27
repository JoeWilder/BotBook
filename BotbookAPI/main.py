from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from sqlalchemy.orm import Session
import time
import random
from datetime import datetime
import uuid

from .SQLPackage import crud, models, schemas, PostGenerator
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




# Function to create a new post
def create_post(db: Session, author_id: str, username: str, name: str, body: str):
    post = models.Post(postId=str(uuid.uuid4()), authorId=author_id, username=username, name=name, body=body, createdAt=datetime.utcnow())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

# Function to create a new post
def create_comment(db: Session, post_id: str, author_id: str, body: str):
    comment = models.Comment(commentId=str(uuid.uuid4()), postId=post_id, authorId=author_id, body=body, createdAt=datetime.utcnow())
    db.add(comment)
    db.commit()
    db.refresh(comment)


@app.on_event("startup")
@repeat_every(seconds=45)
def content_creation_task():
    # We can only query the database from within a fastapi route, so we must make a new session
    db = next(get_db())
    try:
        random_user = crud.get_random_user(db)
        print(f"Creating post: {random_user.__dict__}")
        post_content = PostGenerator.GeneratePost("-passionate\n-excited", "hiking")
        post = create_post(db, random_user.userId, random_user.username, random_user.name, post_content)
        random_number = random.randint(0, 3)
        print(f"Creating {random_number} comments")
        for i in range(random_number):
            random_user = crud.get_random_user(db)
            print(f"Creating comment from {random_user.__dict__}")
            comment_content = PostGenerator.GenerateComment("-tired\n-supportive", post.body)
            print(f"post: {post}")
            create_comment(db, post.postId, random_user.userId, comment_content)

    except Exception as e:
        print(e)
    finally:
        db.close()



