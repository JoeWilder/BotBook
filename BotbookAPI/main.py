from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks, Header, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from fastapi_utils.tasks import repeat_every

from sqlalchemy.orm import Session
from sqlalchemy.sql import text

import random
import uuid
from datetime import datetime, timedelta

from .SQLPackage import crud, models, schemas, PostGenerator
from .SQLPackage.database import SessionLocal

from typing import Annotated, List

# Command to start API: uvicorn BotbookAPI.main:app --reload

# Initialize API application
app = FastAPI()

origins = ["*", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# WE NEED TO MAKE SURE TO MAKE A NEW KEY AND PUT IT IN A CONFIG FILE LATER
SECRET_KEY = "enter-long-string-of-random-characters-here"
TOKEN_EXPIRE_MINUTES = 30

@app.post("/token/")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = form_data.username
    password = form_data.password

    login_result = crud.verify_login(db, username, password)
    print(login_result)
    if login_result is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generate a JWT token
    token_expires = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    token_payload = {"sub": login_result, "exp": token_expires}
    token = jwt.encode(token_payload, SECRET_KEY, algorithm="HS256")

    return {"access_token": token, "token_type": "bearer"}

@app.post("/verify-password")
def verify_password(
    data: dict,
    db: Session = Depends(get_db),
):
    
    owner_id = data.get("owner_id")
    password = data.get("password")
    new_password = data.get("new_password")


    if crud.verify_password(db, owner_id, password, new_password) is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return {"message": "Password successfully change"}




@app.post("/signup/")
def signup_user(
    email: str = Header(..., description="Email"),
    username: str = Header(..., description="Username"),
    password: str = Header(..., description="Password"),
    db: Session = Depends(get_db),
):
    if crud.owner_exists(db, username) is True:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_owner = crud.create_owner(db, str(uuid.uuid4()), email, username, username, password)
    return {"message": "User created successfully", "user": new_owner}

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts/", response_model=list[schemas.PostResponse])
def read_all_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_all_posts(db, skip=skip, limit=limit)
    return posts

@app.get("/comments/{post_id}", response_model=list[schemas.Comment])
def read_all_post_comments(post_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = crud.get_comments_for_post(db, post_id=post_id, skip=skip, limit=limit)
    return comments

@app.get("/profilepicture/{user_id}", response_model=str)
def read_profile_pictures(user_id: str, db: Session = Depends(get_db)):
    filename = crud.get_profile_picture_filename(db, user_id=user_id)
    return filename

@app.put("/update-emotion/")
def update_user_emotion(
    user_id: str,
    current_emotion: str = Header(..., description="Current Emotion"),
    new_emotion: str = Header(..., description="New Emotion"),
    db: Session = Depends(get_db),
):
    updated_user_emotion = crud.update_user_emotion(db, user_id, current_emotion, new_emotion)
    return {"message": "User emotion updated successfully", "updated_user_emotion": updated_user_emotion}

@app.post("/add-emotion/")
def add_user_emotion(
    user_id: str,
    emotion: str = Header(..., description="Emotion to Add"),
    db: Session = Depends(get_db),
):
    new_emotion = crud.create_emotion(db, user_id, emotion)
    return {"message": "Emotion added successfully", "new_emotion": new_emotion}

@app.delete("/delete-emotion/", status_code=status.HTTP_200_OK)
def delete_user_emotion(
    user_id: str,
    emotion: str = Header(..., description="Emotion to Delete"),
    db: Session = Depends(get_db),
):
    deleted_Emotion = crud.delete_user_emotion(db, user_id, emotion)
    return {"message": "Interest deleted successfully", "deleted_interest": deleted_Emotion}
    
@app.put("/update-interest/", status_code=status.HTTP_200_OK)
def update_user_interest(
    user_id: str,
    current_interest: str = Header(..., description="Current Interest"),
    new_interest: str = Header(..., description="New Interest"),
    db: Session = Depends(get_db),
):
    updated_user_interest = crud.update_user_interest(db, user_id, current_interest, new_interest)
    return {"message": "User interest updated successfully", "updated_user_interest": updated_user_interest}

@app.post("/add-interest/", status_code=status.HTTP_201_CREATED)
def add_user_interest(
    user_id: str,
    interest: str = Header(..., description="Interest to Add"),
    db: Session = Depends(get_db),
):
    new_interest = crud.create_interest(db, user_id, interest)
    return {"message": "Interest added successfully", "new_interest": new_interest}

@app.delete("/delete-interest/", status_code=status.HTTP_200_OK)
def delete_user_interest(
    user_id: str,
    interest: str = Header(..., description="Interest to Delete"),
    db: Session = Depends(get_db),
):
    deleted_interest = crud.delete_user_interest(db, user_id, interest)
    return {"message": "Interest deleted successfully", "deleted_interest": deleted_interest}

@app.put("/update-name/")
def update_user_name(
    user_id: str,
    new_name: str = Header(..., description="New Name"),
    db: Session = Depends(get_db),
):
    updated_user_name = crud.update_user_name(db, user_id, new_name)
    return {"message": "User emotion updated successfully", "updated_user_emotion": updated_user_name}

@app.get("/emotions/{user_id}", response_model=list[schemas.Emotion])
def read_all_emotions(user_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    emotions = crud.get_emotions_for_user(db, user_id=user_id, skip=skip, limit=limit)
    return emotions

@app.get("/user-info/{user_id}", response_model=schemas.User)
def read_all_interests(user_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user = crud.get_user_info(db, user_id=user_id, skip=skip, limit=limit)
    return user

@app.get("/interests/{user_id}", response_model=list[schemas.Interest])
def read_all_interests(user_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    interests = crud.get_interest_for_user(db, user_id=user_id, skip=skip, limit=limit)
    return interests

@app.post("/add-user/")
def add_user_user(
    data: dict,
    db: Session = Depends(get_db),
):
    owner_id = data.get("owner_id")
    name = data.get("name")
    username = data.get("username")
    profile_picture = data.get("profile_picture")
    interests = data.get("interests")
    emotions = data.get("emotions")
    new_user = crud.create_user(db, owner_id, username, name, profile_picture)

    for interest in interests:
        crud.create_interest(db, new_user.userId, interest.get("value"))
        print("Added " + interest.get("value"))

    for emotion in emotions:
        crud.create_emotion(db, new_user.userId, emotion.get("value"))
        print("Added " + emotion.get("value"))
    
    return {"message": "User added successfully", "new_user": new_user}

@app.delete("/delete-user/")
def delete_user(
    data: dict,
    db: Session = Depends(get_db),
):
    userId = data.get("user_id")

    interests = crud.get_interest_for_user(db, userId, 0, 100)
    for interest in interests:
        crud.delete_user_interest(db, userId, interest.interest)

    emotions = crud.get_emotions_for_user(db, userId, 0, 100)
    for emotion in emotions:
        crud.delete_user_emotion(db, userId, emotion.emotion)

    message = crud.delete_user(db, userId)

    return {"message": "User successfully deleted"}



@app.get("/owner/{owner_id}", response_model=schemas.OwnerData)
def get_owner_data_test(owner_id: str, db: Session = Depends(get_db)):
    owner_data = crud.get_owner_data(db, owner_id)
    print(owner_data)
    return owner_data

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
