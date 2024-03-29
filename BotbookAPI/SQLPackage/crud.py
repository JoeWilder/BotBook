from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import func, text, update, delete
from . import models, schemas

import time
import random
from datetime import datetime
import uuid
import pytz
import random

from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def get_all_posts(db: Session, skip: int, limit: int):
    posts = db.query(models.Post).offset(skip).limit(limit).all()

    for post in posts:
        post.createdAt = str(post.createdAt)
    return posts

def get_posts_between_times(db: Session, start_time: str, end_time: str):
    posts = db.query(models.Post).filter(models.Post.createdAt.between(start_time, end_time)).all()

    for post in posts:
        post.createdAt = str(post.createdAt)
    return posts

def get_comments_for_post(db: Session, post_id: str, skip: int, limit: int):
    comments = db.query(models.Comment).filter(models.Comment.postId == post_id).offset(skip).limit(limit).all()

    for comment in comments:
        comment.createdAt = str(comment.createdAt)

    return comments

def get_profile_picture_filename(db: Session, user_id: str):
    filename = db.query(models.User.profilePictureFilename).filter(models.User.userId == user_id).scalar()
    return filename


def get_user_count(db: Session):
    count = db.query(func.count(models.User.userId)).scalar()
    
    return count

def get_post_count_between_times(db: Session, start_time: str, end_time: str):
    count = db.query(func.count(models.Post.postId)).filter(models.Post.createdAt.between(start_time, end_time)).scalar()

    return count

def get_random_user(db: Session, number_users: int):
    random_offset = random.randint(0, number_users - 1)
    user = db.query(models.User.userId, models.User.name, models.User.username).offset(random_offset).limit(1).all()

    return user

def get_user_emotion(db: Session, user_id: str):
    list_emotions = db.query(models.Emotion.emotion).filter(models.Emotion.userId == user_id).all()
    random_emotion = random.choice(list_emotions)

    return random_emotion

def get_user_interest(db: Session, user_id: str):
    list_interests = db.query(models.Interest.interest).filter(models.Interest.userId == user_id).all()
    random_interest = random.choice(list_interests)

    return random_interest

def create_post(db: Session, author_id: str, username: str, name: str, body: str):

    est_timezone = pytz.timezone('US/Eastern')
    est_now = datetime.now(est_timezone)

    post = models.Post(postId=str(uuid.uuid4()), authorId=author_id, username=username, name=name, body=body, createdAt=est_now)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def create_comment(db: Session, post_id: str, author_id: str, username: str, name: str, body: str):

    est_timezone = pytz.timezone('US/Eastern')
    est_now = datetime.now(est_timezone)

    comment = models.Comment(commentId=str(uuid.uuid4()), postId=post_id, authorId=author_id, username=username, name=name, body=body, createdAt=est_now)
    db.add(comment)
    db.commit()
    db.refresh(comment)

def update_user_interest(db: Session, user_id: str, current_interest: str, new_interest: str):
    stmt = (
        update(models.Interest)
        .where(
            (models.Interest.userId == user_id) &
            (models.Interest.interest == current_interest)
        )
        .values(interest=new_interest)
        .execution_options(synchronize_session="fetch")
    )

    try:
        # Execute the update statement
        db.execute(stmt)

        # Commit the changes to the database
        db.commit()

        # Fetch the updated result
        updated_user_interest = db.query(models.Interest).filter(
            models.Interest.userId == user_id,
            models.Interest.interest == new_interest
        ).first()

        if updated_user_interest:
            return updated_user_interest
        else:
            raise HTTPException(status_code=404, detail="User and interest not found")

    except Exception as e:
        # Handle exceptions and rollback changes on error
        db.rollback()
        raise e
    
def create_interest(db: Session, user_id: str, interest: str):
    user_interest = models.Interest(userId=user_id, interest=interest)
    db.add(user_interest)
    db.commit()
    db.refresh(user_interest)
    return user_interest

def delete_user_interest(db: Session, user_id: str, interest: str):
    stmt = (
        delete(models.Interest)
        .where(
            (models.Interest.userId == user_id) &
            (models.Interest.interest == interest)
        )
        .execution_options(synchronize_session="fetch")
    )

    db.execute(stmt)

    db.commit()

    deleted_user_interest = db.query(models.Interest).filter(
            models.Interest.userId == user_id,
            models.Interest.interest == interest
        ).first()

    if not deleted_user_interest:
        pass
    else:
        raise HTTPException(status_code=404, detail="User and interest not found")
    
def update_user_emotion(db: Session, user_id: str, current_emotion: str, new_emotion: str):
    stmt = (
        update(models.Emotion)
        .where(
            (models.Emotion.userId == user_id) &
            (models.Emotion.emotion == current_emotion)
        )
        .values(emotion=new_emotion)
        .execution_options(synchronize_session="fetch")
    )

    try:
        # Execute the update statement
        db.execute(stmt)

        # Commit the changes to the database
        db.commit()

        # Fetch the updated result
        updated_user_emotion = db.query(models.Emotion).filter(
            models.Emotion.userId == user_id,
            models.Emotion.emotion == new_emotion
        ).first()

        if updated_user_emotion:
            return updated_user_emotion
        else:
            raise HTTPException(status_code=404, detail="User and emotion not found")

    except Exception as e:
        # Handle exceptions and rollback changes on error
        db.rollback()
        raise e
    
def create_emotion(db: Session, user_id: str, emotion: str):
    user_emotion = models.Emotion(userId=user_id, emotion=emotion)
    db.add(user_emotion)
    db.commit()
    db.refresh(user_emotion)
    return user_emotion

def delete_user_emotion(db: Session, user_id: str, emotion: str):
    stmt = (
        delete(models.Emotion)
        .where(
            (models.Emotion.userId == user_id) &
            (models.Emotion.emotion == emotion)
        )
        .execution_options(synchronize_session="fetch")
    )

    db.execute(stmt)
    db.commit()

    deleted_user_emotion = db.query(models.Emotion).filter(
        models.Emotion.userId == user_id,
        models.Emotion.emotion == emotion
    ).first()

    if not deleted_user_emotion:
        pass
    else:
        raise HTTPException(status_code=404, detail="User and emotion not found")


def get_all_posts(db: Session, skip: int = 0, limit: int = 100):
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

def update_user_name(db: Session, user_id: str, new_name):
    stmt = (
        update(models.User)
        .where(
            (models.User.userId == user_id)
        )
        .values(name=new_name)
        .execution_options(synchronize_session="fetch")
    )

    try:
        # Execute the update statement
        db.execute(stmt)

        # Commit the changes to the database
        db.commit()

        # Fetch the updated result
        updated_user_name = db.query(models.User).filter(
            models.User.userId == user_id
        ).first()

        if updated_user_name:
            return updated_user_name
        else:
            raise HTTPException(status_code=404, detail="User and emotion not found")

    except Exception as e:
        # Handle exceptions and rollback changes on error
        db.rollback()
        raise e
    
def get_emotions_for_user(db: Session, user_id: str, skip: int, limit: int):
    emotions = db.query(models.Emotion).filter(models.Emotion.userId == user_id).all()
    
    return emotions

def get_interest_for_user(db: Session, user_id: str, skip: int, limit: int):
    interests = db.query(models.Interest).filter(models.Interest.userId == user_id).all()
    
    return interests

def get_user_info(db: Session, user_id: str, skip: int, limit: int):
    user = db.query(models.User).filter(models.User.userId == user_id).first()

    user.createdAt = str(user.createdAt)

    return user

def create_user(db: Session, owner_id: str, username:str, name:str, profile_picture:str):
    if not profile_picture:
        profile_picture = "default.jfif"

    user = models.User(ownerId=owner_id, username=username, name=name, createdAt=datetime.now(), profilePictureFilename=profile_picture)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: str):
    user = db.query(models.User).filter(models.User.userId == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}

def create_owner(db: Session, owner_id: str, email:str, username:str, name:str, password:str, createdAt=datetime.now()):
    hashed_password = pwd_context.hash(password)
    owner = models.Owner(ownerId=owner_id, email=email, password=hashed_password, username=username, name=name, createdAt=datetime.now(), profilePictureFilename="defaultprofilepicture.jpg")
    db.add(owner)
    db.commit()
    db.refresh(owner)
    return owner

def update_owner_profile_picture(db: Session, owner_id: str, newProfilePictureFilename: str):
    db.execute(
        update(models.Owner)
        .where(models.Owner.ownerId == owner_id)
        .values(profilePictureFilename=newProfilePictureFilename)
    )
    db.commit()

def owner_exists(db: Session, username: str) -> bool:
    return db.query(models.Owner).filter(models.Owner.username == username).first() is not None

def get_owner_data(db: Session, owner_id: str):

    query = text("""
                SELECT o.email, 
                        o.name AS owner_name,
                        o.profilePictureFilename AS owner_profile_picture, 
                        o.createdAt AS owner_created_at,
                        b.userId AS bot_id, 
                        b.name AS bot_name, 
                        b.createdAt AS bot_creation_date, 
                        b.profilePictureFilename AS profile_file_name,
                        GROUP_CONCAT(DISTINCT i.interest SEPARATOR '|') AS interests,
                        GROUP_CONCAT(DISTINCT e.emotion SEPARATOR '|') AS emotions
                    FROM owners o
                    LEFT JOIN users b ON o.ownerId = b.ownerId
                    LEFT JOIN interests i ON b.userId = i.userId
                    LEFT JOIN emotions e ON b.userId = e.userId
                    WHERE o.ownerId = :owner_id
                    GROUP BY o.ownerId, b.userId
            """)
    
    owner_data = db.execute(query.bindparams(owner_id=owner_id)).fetchall()

    owner_info = {
            'email': owner_data[0]['email'],
            'name': owner_data[0]['owner_name'],
            'profilePictureFilename': owner_data[0]['owner_profile_picture'],
            'createdAt': owner_data[0]['owner_created_at'],
            'bots': []
        }
    
    for row in owner_data:
            bot_info = {
                'userId' : row['bot_id'],
                'name': row['bot_name'],
                'createdAt': row['bot_creation_date'],
                'profilePictureFilename': row['profile_file_name'],
                'interests': row['interests'].split('|') if row['interests'] else [],
                'emotions': row['emotions'].split('|') if row['emotions'] else []
            }
            owner_info['bots'].append(bot_info)

    print(owner_data[0]['owner_profile_picture'])

    return owner_info


    #print("OWNER ID: " + owner_id)
    #return db.query(models.Owner).filter(models.Owner.ownerId == owner_id).first()


def verify_login(db: Session, username: str, password: str):
    user = db.query(models.Owner).filter(models.Owner.username == username).first()
    
    # If the user doesn't exist, return False
    if not user:
        return None
    
    
    try:
        if not pwd_context.verify(password, user.password):
            return None
    except Exception as e:
        return None
    
    # User authenticated successfully
    return user.ownerId

# If correct password, update to new password
def verify_password(db: Session, owner_id: str, password: str, new_password: str):
    user = db.query(models.Owner).filter(models.Owner.ownerId == owner_id).first()

    try:
        if not pwd_context.verify(password, user.password):
            return None
    except Exception as e:
        return None

    user.password = pwd_context.hash(new_password)
    db.commit()
    
    return user.ownerId