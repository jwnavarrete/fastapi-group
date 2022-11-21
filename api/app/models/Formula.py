from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from ..database import Base


class FormulaModel(Base):
    __tablename__ = 'formula'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("UserModel")
    version = Column(String, nullable=False)
    estado = Column(String(1), nullable=False)        
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))