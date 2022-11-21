from sqlalchemy import Column, Integer, String
from ..database import Base

class PerfilModel(Base):
    __tablename__ = 'perfil'
    id = Column(Integer, primary_key=True, nullable=False)
    descripcion = Column(String(250), nullable=False)
    estado = Column(String(1), nullable=False)
    