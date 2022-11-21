from sqlalchemy import  Column, Integer, String
from ..database import Base


class CategoryModel(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)