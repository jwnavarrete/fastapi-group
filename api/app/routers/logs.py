from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import func
from .. import oauth2
from ..schemas.log import LogsResponse, LogCreate
from ..models.Log import LogModel 
from ..models.User import UserModel 
from ..database import get_db
from sqlalchemy.sql import select

router = APIRouter(
    prefix="/logs",
    tags=['Logs']
)

@router.get("/", response_model=List[LogsResponse])
def get_logs(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), fecdesde: str= '', fechasta: str = ''):
    data = db.query(LogModel).filter(func.date(LogModel.created_at)>=fecdesde, func.date(LogModel.created_at)<=fechasta).order_by(LogModel.created_at.desc()).all()
    return data


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=LogsResponse)
def create_logs(log: LogCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_log = LogModel(owner_id=current_user.id, **log.dict())
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log
