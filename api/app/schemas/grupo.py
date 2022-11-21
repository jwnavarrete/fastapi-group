from pydantic import BaseModel


class GrupoResponse(BaseModel):
    id: int
    nombre: str
    estado: str
    
    class Config:
        orm_mode = True
