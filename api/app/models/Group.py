from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from ..database import Base

class GroupModel(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True, nullable=False)
    user_creator = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    title = Column(String, nullable=False)
    detail = Column(String, nullable=False)
    # TABLAS RELACIONALES
    # TABLA DE PRIVACIDAD
    privacy_id = Column(Integer, ForeignKey("privacy.id", ondelete="CASCADE"), nullable=False)
    privacy = relationship("PrivacyModel")
    # TABLA DE CATEGORIAS
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    category = relationship("CategoryModel")
    
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))