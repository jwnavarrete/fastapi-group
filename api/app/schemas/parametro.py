from pydantic import BaseModel

class ParametroCreate(BaseModel): 
    nombre : str
    tipo: int
    estado: str
    
class ParametroUpdate(BaseModel): 
    nombre : str
    tipo: str
    estado: str
    
class ParametroResponse(ParametroCreate):
    id: int
    class Config:
        orm_mode = True