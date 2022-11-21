from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr
from pydantic.types import conint
from app.database import Base

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    perfil_id: int

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    perfil_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email : EmailStr
    password: str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str]

class PostBase(BaseModel):
    title : str
    content: str
    published: bool = True

class PerfilBase(BaseModel):
    descripcion: str
    estado: str

class LogsBase(BaseModel):
    actividad: str
    user_id: str
    fecha: datetime

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


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


class PerfilResponse(PerfilBase):
    id: int
    descripcion: str
    estado: str

    class Config:
        orm_mode = True


class PerfilCreate(PerfilBase):
    descripcion: str
    estado: str

class PerfilUpdate(PerfilBase):
    descripcion : str
    estado: str
    
class LogsBase(BaseModel):
    actividad : str
    owner_id: int    
    
class LogsResponse(LogsBase):
    id: int
    actividad : str
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True
        
class LogCreate(LogsBase):
    actividad: str
    owner_id: str
    
# TODO ESTO ES PARA FORMULA 

    
class FormulaCreate(BaseModel): 
    version : str
    user_id: int
    estado: str
    
class FormulaUpdate(BaseModel): 
    version : str
    estado: str
    
class FormulaResponse(FormulaCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class TipoResponse(BaseModel):
    id:int
    nombre:str
    estado:str
    class Config:
        orm_mode = True

class TipoCreate(BaseModel):
    nombre:str
    estado:str

class TipoUpdate(BaseModel):
    nombre:str
    estado:str

class RubroResponse(BaseModel):
    id:int
    nombre:str
    estado:str
    class Config:
        orm_mode = True

class RubroCreate(BaseModel):
    nombre:str
    estado:str

class RubroUpdate(BaseModel):
    nombre:str
    estado:str    
