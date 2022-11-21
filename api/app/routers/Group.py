from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from .. import utils
from ..schemas.Group import GroupCreate, GroupUpdate, GroupResponse
from ..models.Group import GroupModel
from ..database import get_db
from ..Lib.general import modelDataExistById

router = APIRouter(
    prefix="/group",
    tags=['Group']
)

@router.get("/", response_model=List[GroupResponse])
def get_all(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), title : Optional[str] = ""):
    users = db.query(GroupModel).filter(GroupModel.title.ilike(f'%{ title}%')).all()
    return users


@router.get('/{id}', response_model=GroupResponse)
def get_one(id: int, db: Session = Depends(get_db), ):
    data = db.query(GroupModel).filter(GroupModel.id == id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Group with id: {id} does not exist")
    return data


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=GroupResponse)
def create(data: GroupCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data.user_creator = current_user

    new_data = GroupModel(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data

@router.patch("/{id}", response_model=GroupResponse)
def update(id: int, dataUpate: GroupUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(GroupModel).filter(GroupModel.id == id)
    data = post_query.first()

    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Group with id: {id} does not exist")

    update_data = dataUpate.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)
    db.commit()
    return post_query.first()