from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from sqlalchemy.orm import Session

import random

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

@app.get("/profilepicture/{user_id}", response_model=str)
def read_profile_pictures(user_id: str, db: Session = Depends(get_db)):
    filename = crud.get_profile_picture_filename(db, user_id=user_id)
    return filename


@app.on_event("startup")
@repeat_every(seconds=45 * 5)
def content_creation_task():
    # We can only query the database from within a fastapi route, so we must make a new session
    db = next(get_db())
    try:
        number_users = crud.get_user_count(db)
        random_poster = crud.get_random_user(db, number_users)

        print(f"Creating post: {random_poster}")
        print(random_poster[0][0])

        user_interest = crud.get_user_interest(db, random_poster[0][0])
        user_emotion = crud.get_user_emotion(db, random_poster[0][0])

        print(user_emotion)
        print(user_interest)


        post_content = PostGenerator.GeneratePost(f"-{str(user_emotion)}", str(user_interest))
        post = crud.create_post(db, random_poster[0][0], random_poster[0][2], random_poster[0][1], post_content)

        random_number = random.randint(0, 3)
        print(f"Creating {random_number} comments")

        for i in range(random_number):
            random_user = crud.get_random_user(db, number_users)

            if (random_user[0][0] == random_poster[0][0]):
                print("Blocking author from commenting on their own post")
                continue

            user_emotion = crud.get_user_emotion(db, random_user[0][0])
            
            print(f"Creating comment from {random_user}")
            print(user_emotion)

            comment_content = PostGenerator.GenerateComment(f"-{str(user_emotion)}", post.body)
            print(f"post: {post}")
            crud.create_comment(db, post.postId, random_user[0][0], random_user[0][2], random_user[0][1], comment_content)
        
    except Exception as e:
        print(e)
    finally:
        db.close()



