from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

import time
import random
from datetime import datetime
import uuid
import pytz
import random

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