from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class RubroModel(Base):
    __tablename__='rubro'
    id = Column(Integer, primary_key=True, nullable=False)
    codigo=Column(String(10), nullable=False)
    nombre=Column(String(250), nullable=False)
    estado=Column(String(1), nullable=False) 
    tipo_id = Column(Integer, ForeignKey("tipo.id", ondelete="CASCADE"), nullable=False)
    tipo = relationship("TipoModel")
