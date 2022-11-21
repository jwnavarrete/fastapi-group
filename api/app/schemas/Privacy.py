from pydantic import BaseModel

class PrivacyResponse(BaseModel):
    id: int
    name: str
    
    class Config:
        orm_mode = True