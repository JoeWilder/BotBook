from pydantic import BaseModel, AnyHttpUrl, EmailStr
from typing import List

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

class PostBase(BaseModel):
    authorId: str
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
    friends: List[Friend] = []
    interests: List[Interest] = []
    posts: List[Post] = []
    comments: List[Comment] = []

    class Config:
        orm_mode = True