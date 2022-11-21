from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from ..schemas.grupo import GrupoResponse
from ..models.Grupo import GrupoModel
from ..database import get_db

router = APIRouter(
    prefix="/grupo",
    tags=['Grupo']
)

@router.get("/", response_model=List[GrupoResponse])
def get_Grupo(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0):
    grupo = db.query(GrupoModel).limit(limit).offset(offset).all()
    return grupo


@router.get("/{id}", response_model=GrupoResponse)
def get_id(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(GrupoModel).filter(GrupoModel.id == id)

    grupo = post_query.first()

    if grupo == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"grupo with id: {id} does not exist")
    return grupo