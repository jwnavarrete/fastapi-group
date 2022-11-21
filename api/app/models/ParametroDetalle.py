from sqlalchemy import Column, Integer, Float, String, ForeignKey
from ..database import Base
from sqlalchemy.orm import relationship

class ParametroDetalleModel(Base):
    __tablename__ = 'parametro_detalle'
    id = Column(Integer, primary_key=True, nullable=False)
    parametro_id = Column(Integer, ForeignKey("parametro.id", ondelete="CASCADE"), nullable=False)
    parametro = relationship("ParametroModel")
    # grupo = Column(String, nullable=True)
    grupo_id = Column(Integer, ForeignKey("grupo.id", ondelete="CASCADE"), nullable=True)
    grupo = relationship("GrupoModel")
    
    # subgrupo = Column(String, nullable=True)
    sub_grupo_id = Column(Integer, ForeignKey("sub_grupo.id", ondelete="CASCADE"), nullable=True)
    sub_grupo = relationship("SubGrupoModel")
        
    rango = Column(String, nullable=True)
    desde = Column(Float, nullable=True)
    hasta = Column(Float, nullable=True)
    factor = Column(Float(7))