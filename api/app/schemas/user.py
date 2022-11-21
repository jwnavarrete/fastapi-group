from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    estado: str
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    estado: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email : EmailStr
    password: str


class UserUpdate(BaseModel):
    email: EmailStr
    password: str
    estado: str