from sqlalchemy import Column, Integer, String
from ..database import Base

class TipoModel(Base):
    __tablename__='tipo'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre=Column(String(250), nullable=False)
    estado=Column(String(1), nullable=False)
    medida=Column(String(1), nullable=False)
