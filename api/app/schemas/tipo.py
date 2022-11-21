from pydantic import BaseModel

class TipoResponse(BaseModel):
    id:int
    nombre:str
    medida:str
    estado:str
    class Config:
        orm_mode = True

class TipoCreate(BaseModel):
    medida:str
    nombre:str
    estado:str

class TipoUpdate(BaseModel):
    medida:str
    nombre:str
    estado:str
