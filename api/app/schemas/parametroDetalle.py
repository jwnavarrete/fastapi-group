from pickletools import int4
from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr
from .parametro import ParametroResponse
from typing import Optional
from .grupo import GrupoResponse
from .subGrupo import SubGrupoResponse

class ParametroDetalleCreate(BaseModel):
    parametro_id: int
    grupo_id: Optional[int]
    sub_grupo_id: Optional[int]
    rango: Optional[str]
    desde: Optional[float]
    hasta: Optional[float]
    factor: float

class ParametroDetalleResponse(ParametroDetalleCreate):
    id: int
    parametro: ParametroResponse
    grupo: Optional[GrupoResponse]
    sub_grupo: Optional[SubGrupoResponse]
    
    class Config:
        orm_mode = True

class ParametroDetalleUpdate(BaseModel):
    parametro_id: int
    grupo_id: Optional[int]
    sub_grupo_id: Optional[int]
    rango: Optional[str]
    desde: Optional[float]
    hasta: Optional[float]
    factor: float
