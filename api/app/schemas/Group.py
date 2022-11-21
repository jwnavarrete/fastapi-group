from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .user import UserResponse 
from .Privacy import PrivacyResponse
from .Category import CategoryResponse

class GroupCreate(BaseModel):
    name: str
    title: str
    detail: str
    privacy_id: int
    category_id: int
    
# DEBE PERMITIR CAMBIAR ?
class GroupUpdate(BaseModel):
    name: Optional[str] 
    title: Optional[str]
    detail: Optional[str]
    privacy_id: Optional[int]
    category_id: Optional[int]
    
class GroupResponse(BaseModel):
    id: int
    name: str
    # CAMPO USER_CREATOR Y RELACION CON EL SCHEMA
    user_creator: int
    user: UserResponse
    
    title: str
    detail: str
    # CAMPO PRIVACIDAD Y RELACION CON EL SCHEMA
    privacy_id: int
    privacy: PrivacyResponse
    # CAMPO CATEGORIA Y RELACION CON EL SCHEMA
    category_id: int
    category: CategoryResponse
    
    created_at: datetime

    class Config:
        orm_mode = True
