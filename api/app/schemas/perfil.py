from pydantic import BaseModel

class PerfilBase(BaseModel):
    descripcion: str
    estado: str

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