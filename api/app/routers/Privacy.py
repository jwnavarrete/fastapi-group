from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from .. import utils
from ..schemas.Privacy import PrivacyResponse
from ..models.Privacy import PrivacyModel
from ..database import get_db
from ..Lib.general import modelDataExistById

router = APIRouter(
    prefix="/privacy",
    tags=['Privacy']
)

@router.get("/", response_model=List[PrivacyResponse])
def get_all(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    users = db.query(PrivacyModel).all()
    return users