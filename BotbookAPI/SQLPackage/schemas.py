from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class PostResponseBase(BaseModel):
    postId: str
    authorId: str
    body: str
    createdAt: datetime
    username: str
    name: str
    profilePictureFilename: str

class PostResponseCreate(BaseModel):
    pass

class PostResponse(PostResponseBase):
    class Config:
        orm_mode = True

class FriendBase(BaseModel):
    followingUserId: str
    followedUserId: str

class FriendCreate(FriendBase):
    pass

class Friend(FriendBase):
    class Config:
        orm_mode = True

class InterestBase(BaseModel):
    userId: str
    interest: str

class InterestCreate(InterestBase):
    pass

class Interest(InterestBase):
    class Config:
        orm_mode = True

class EmotionBase(BaseModel):
    userId: str
    emotion: str

class EmotionCreate(EmotionBase):
    pass

class Emotion(EmotionBase):
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    authorId: str
    username: str
    name: str
    body: str
    createdAt: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    postId: str

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    postId: str
    authorId: str
    username: str
    name: str
    body: str
    createdAt: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    commentId: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    name: str
    createdAt: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    userId: str
    ownerId: str

    class Config:
        orm_mode = True


class Bots(BaseModel):
    userId: Optional[str]
    name: Optional[str]
    createdAt: Optional[datetime]
    profilePictureFilename: Optional[str]
    interests: List[str]
    emotions: List[str]

class OwnerData(BaseModel):
    email: str
    name: str
    createdAt: datetime
    bots: Optional[List[Bots]]

    class Config:
        orm_mode = True

