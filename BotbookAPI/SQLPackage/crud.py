from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
import random

def get_all_posts(db: Session, skip: int, limit: int):
    posts = db.query(models.Post).offset(skip).limit(limit).all()

    get_random_user(db)

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


def get_random_user(db: Session):
    items = db.query(models.User).all()
    random_item = random.choice(items)
    return random_item