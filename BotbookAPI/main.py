from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_utils.tasks import repeat_every

from jose import JWTError, jwt
from passlib.context import CryptContext

from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from datetime import datetime, timedelta
import random

from .SQLPackage import crud, models, schemas, PostGenerator
from .SQLPackage.database import SessionLocal

from typing import Annotated

# Command to start API: uvicorn BotbookAPI.main:app --reload

SECRET_KEY = "73e204ac4d1dd633235379b51cbd6fe8"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    pass

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    
    return user

def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    

@app.get("/posts/", response_model=list[schemas.PostResponse])
def read_all_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = text("""
        SELECT 
            p.postId,
            p.authorId,
            p.body,
            p.createdAt,
            u.username,
            u.name,
            u.profilePictureFilename
        FROM posts AS p 
            INNER JOIN users AS u ON u.userId = p.authorId
        LIMIT :limit OFFSET :skip
    """)
    
    posts = db.execute(query.bindparams(limit=limit, skip=skip)).fetchall()

    result = [
        {
            "postId": post.postId,
            "authorId": post.authorId,
            "body": post.body,
            "createdAt": post.createdAt,
            "username": post.username,
            "name": post.name,
            "profilePictureFilename": post.profilePictureFilename,
        }
        for post in posts
    ]

    return result

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
