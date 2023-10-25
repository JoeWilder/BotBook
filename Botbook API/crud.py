from sqlalchemy.orm import Session
from . import models, schemas

def get_all_posts(db: Session):
    return db.query(models.Post).all()

def get_posts_between_times(db: Session, start_time: str, end_time: str):
    return db.query(models.Post).filter(models.Post.createdAt.between(start_time, end_time)).all()

def get_comments_for_post(db: Session, post_id: str):
    return db.query(models.Comment).filter(models.Comment.postId == post_id).all()
