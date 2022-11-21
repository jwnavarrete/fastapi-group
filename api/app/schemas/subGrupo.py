from pydantic import BaseModel
from .grupo import GrupoResponse

class SubGrupoResponse(BaseModel):
    id: int
    nombre: str
    estado: str
    grupo: GrupoResponse
    
    class Config:
        orm_mode = True
