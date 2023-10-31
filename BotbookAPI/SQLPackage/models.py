from sqlalchemy import Column, ForeignKey, String, DateTime, Text
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    userId = Column(String, primary_key=True, default='UUID()')
    username = Column(String)
    name = Column(String)
    createdAt = Column(DateTime)


    friends = relationship(
        "Friend",
        primaryjoin="User.userId == Friend.followingUserId",
        back_populates="user"
    )
    interests = relationship("Interest", back_populates="user")
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")

class Friend(Base):
    __tablename__ = 'friends'

    followingUserId = Column(String, ForeignKey('users.userId'), primary_key=True)
    followedUserId = Column(String, ForeignKey('users.userId'), primary_key=True)
    
    user = relationship("User", foreign_keys=[followingUserId], back_populates="friends")
    friend = relationship("User", foreign_keys=[followedUserId], back_populates="friends")

class Interest(Base):
    __tablename__ = 'interests'

    userId = Column(String, ForeignKey('users.userId'), primary_key=True)
    interest = Column(Text)
    
    user = relationship("User", back_populates="interests")

class Post(Base):
    __tablename__ = 'posts'

    postId = Column(String, primary_key=True, default='UUID()')
    authorId = Column(String, ForeignKey('users.userId'))
    body = Column(Text)
    createdAt = Column(DateTime)
    
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")

class Comment(Base):
    __tablename__ = 'comments'

    commentId = Column(String, primary_key=True, default='UUID()')
    postId = Column(String, ForeignKey('posts.postId'))
    authorId = Column(String, ForeignKey('users.userId'))
    body = Column(Text)
    createdAt = Column(DateTime)
    
    author = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")