from pydantic import BaseModel
from datetime import datetime
from .user import UserResponse

class FormulaCreate(BaseModel): 
    version : str
    estado: str
    
class FormulaUpdate(BaseModel): 
    version : str
    estado: str
    
class FormulaResponse(FormulaCreate):
    id: int
    user_id: str
    created_at: datetime
    user: UserResponse

    class Config:
        orm_mode = True