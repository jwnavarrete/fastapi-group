from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import Session
from ..database import Base


class MenuModel(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String(50), nullable=False)
    tipo = Column(Integer, nullable=False)
    icono = Column(String(50), nullable=True)        
    url = Column(String(50), nullable=True)        
    parent_id = Column(Integer, ForeignKey("menu.id", ondelete="CASCADE"), nullable=True)
    menu = relationship("MenuModel")