from pydantic import BaseModel
from datetime import datetime
from .user import UserResponse

class LogsBase(BaseModel):
    actividad : str
    owner_id: int    
    
class LogsResponse(LogsBase):
    id: int
    actividad : str
    owner_id: int
    owner: UserResponse
    created_at: datetime
    modulo: str
    
    class Config:
        orm_mode = True
        
class LogCreate(BaseModel):
    actividad: str
    modulo: str