from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base
from sqlalchemy.orm import relationship

class SubGrupoModel(Base):
    __tablename__ = 'sub_grupo'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    grupo_id = Column(Integer, ForeignKey("grupo.id", ondelete="CASCADE"), nullable=False)
    grupo = relationship("GrupoModel")
    estado = Column(String(1), nullable=False)