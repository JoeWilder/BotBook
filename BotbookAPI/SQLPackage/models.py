from sqlalchemy import Column, ForeignKey, String, DateTime, Text
from sqlalchemy.orm import relationship

import uuid

from .database import Base

class Owner(Base):
    __tablename__ = 'owners'

    ownerId = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String)
    password = Column(String)
    username = Column(String)
    name = Column(String)
    createdAt = Column(DateTime)
    profilePictureFilename = Column(String)

class User(Base):
    __tablename__ = 'users'

    userId = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    ownerId = Column(String, ForeignKey('owners.ownerId'))
    username = Column(String)
    name = Column(String)
    createdAt = Column(DateTime)
    profilePictureFilename = Column(String)

class Friend(Base):
    __tablename__ = 'friends'

    followingUserId = Column(String, ForeignKey('users.userId'), primary_key=True)
    followedUserId = Column(String, ForeignKey('users.userId'), primary_key=True)

class Interest(Base):
    __tablename__ = 'interests'

    userId = Column(String, ForeignKey('users.userId'), primary_key=True)
    interest = Column(Text)

class Emotion(Base):
    __tablename__ = 'emotions'

    userId = Column(String, ForeignKey('users.userId'), primary_key=True)
    emotion = Column(Text)

class Post(Base):
    __tablename__ = 'posts'

    postId = Column(String, primary_key=True)
    authorId = Column(String, ForeignKey('users.userId'))
    username = Column(String)
    name = Column(String)
    body = Column(Text)
    createdAt = Column(DateTime)

class PostResponseModel(Base):
    __tablename__ = 'posts'
    
    postId: int
    authorId: int
    body: str
    createdAt: DateTime
    username: str
    name: str
    profilePictureFilename: str

class Comment(Base):
    __tablename__ = 'comments'

    commentId = Column(String, primary_key=True, default='UUID()')
    postId = Column(String, ForeignKey('posts.postId'))
    authorId = Column(String, ForeignKey('users.userId'))
    username = Column(String)
    name = Column(String)
    body = Column(Text)
    createdAt = Column(DateTime)