from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .perfil import PerfilResponse
from .menu import MenuResponse

class MenuPerfilCreate(BaseModel): 
    perfil_id : int
    menu_id: int
    orden: int
    lectura: bool
    escritura: bool
    
class MenuPerfilUpdate(BaseModel): 
    orden: Optional[int]
    lectura: Optional[bool]
    escritura: Optional[bool]
    
class MenuPerfilResponse(BaseModel):
    perfil_id : int
    menu_id: int
    orden: int
    lectura: bool
    escritura: bool
    perfil: PerfilResponse
    menu: MenuResponse

    class Config:
        orm_mode = True