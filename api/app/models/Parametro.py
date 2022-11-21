from sqlalchemy import Column, Integer, String
from ..database import Base

class ParametroModel(Base):
    __tablename__ = 'parametro'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    tipo = Column(Integer, nullable=False)
    estado = Column(String(1), nullable=False)