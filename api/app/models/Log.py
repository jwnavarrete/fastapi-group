from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from ..database import Base
from ..utils import time_now

class LogModel(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, nullable=False)
    actividad = Column(String, nullable=False)    
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=time_now)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("UserModel")
    modulo = Column(String(50), nullable=False)
