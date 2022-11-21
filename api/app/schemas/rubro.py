from pydantic import BaseModel
from .tipo import TipoResponse

class RubroResponse(BaseModel):
    id:int
    tipo_id:int
    tipo: TipoResponse
    codigo:str
    nombre:str
    estado:str
    class Config:
        orm_mode = True

class RubroCreate(BaseModel):
    tipo_id:int
    codigo:str
    nombre:str
    estado:str

class RubroUpdate(BaseModel):
    tipo_id:int
    codigo:str
    nombre:str
    estado:str