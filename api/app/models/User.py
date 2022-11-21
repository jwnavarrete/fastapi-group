from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from ..database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    perfil_id = Column(Integer, ForeignKey("perfil.id", ondelete="CASCADE"), nullable=False)
    perfil = relationship("PerfilModel")
    estado = Column(String(1), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

