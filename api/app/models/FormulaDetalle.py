from xmlrpc.client import Boolean
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from ..database import Base

class FormulaDetalleModel(Base):
    __tablename__ = 'formula_det'
    id = Column(Integer, primary_key=True, nullable=False)
    orden = Column(Integer, nullable=False)
    valor = Column(String, nullable=False)
    visible = Column(Boolean, nullable=False)        
    # CAMPOS JOIN A OTRAS TABLAS 
    formula_id = Column(Integer, ForeignKey("formula.id", ondelete="CASCADE"), nullable=False)
    formula = relationship("FormulaModel")
    rubro_id = Column(Integer, ForeignKey("rubro.id", ondelete="CASCADE"), nullable=False)
    rubro = relationship("RubroModel")
    tipo_id = Column(Integer, ForeignKey("tipo.id", ondelete="CASCADE"), nullable=False)
    tipo = relationship("TipoModel")
