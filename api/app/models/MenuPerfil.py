from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import Session
from ..database import Base


class MenuPerfilModel(Base):
    __tablename__ = 'menu_perfil'
    # id = Column(Integer, primary_key=True, nullable=False)
    perfil_id = Column(Integer, ForeignKey("perfil.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    perfil = relationship("PerfilModel")
    menu_id = Column(Integer, ForeignKey("menu.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    menu = relationship("MenuModel")
    orden = Column(Integer, nullable=False)
    lectura = Column(Boolean, nullable=False)
    escritura = Column(Boolean, nullable=False)