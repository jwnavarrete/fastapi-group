from pydantic import BaseModel
from typing import Optional

class MenuCreate(BaseModel): 
    titulo : str
    tipo: int
    icono: Optional[str]
    url: Optional[str]
    parent_id: Optional[int]
    
class MenuUpdate(BaseModel): 
    titulo : str
    tipo: int
    icono: Optional[str]
    url: Optional[str]
    parent_id: Optional[int]

class MenuParentResponse(BaseModel):
    id: Optional[int]
    titulo : Optional[str]
    tipo: Optional[str]
    url: Optional[str]
    # parent_id: Optional[int]
    
class MenuResponse(BaseModel):
    id: int
    titulo : str
    tipo: int
    icono: Optional[str]
    url: Optional[str]
    parent_id: Optional[int]
    # menu: Optional[MenuParentResponse]

    class Config:
        orm_mode = True