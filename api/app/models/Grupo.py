from sqlalchemy import Column, Integer, String
from ..database import Base

class GrupoModel(Base):
    __tablename__ = 'grupo'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    estado = Column(String(1), nullable=False)