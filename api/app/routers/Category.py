from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from .. import utils
from ..schemas.Category import CategoryResponse
from ..models.Category import CategoryModel
from ..database import get_db
from ..Lib.general import modelDataExistById

router = APIRouter(
    prefix="/category",
    tags=['Category']
)

@router.get("/", response_model=List[CategoryResponse])
def get_all(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    users = db.query(CategoryModel).all()
    return users