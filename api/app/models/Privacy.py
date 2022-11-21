from sqlalchemy import  Column, Integer, String
from ..database import Base


class PrivacyModel(Base):
    __tablename__ = 'privacy'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)