from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr
from .perfil import PerfilResponse

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    estado: str
    perfil_id: int
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    perfil: PerfilResponse
    perfil_id: int
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
    perfil_id: int