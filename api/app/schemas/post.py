from typing import Optional
from pydantic import BaseModel
from datetime import datetime
# IMPORTAMOS EL SCHEMA DE USER
from .user import UserResponse

class PostBase(BaseModel):
    title : str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    title : Optional[str]
    content: Optional[str]
    published: Optional[bool]

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True

class PostVoteResponse(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True