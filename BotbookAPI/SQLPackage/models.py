from sqlalchemy import Column, ForeignKey, String, DateTime, Text
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    userId = Column(String, primary_key=True, default='UUID()')
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

class Comment(Base):
    __tablename__ = 'comments'

    commentId = Column(String, primary_key=True, default='UUID()')
    postId = Column(String, ForeignKey('posts.postId'))
    authorId = Column(String, ForeignKey('users.userId'))
    username = Column(String)
    name = Column(String)
    body = Column(Text)
    createdAt = Column(DateTime)