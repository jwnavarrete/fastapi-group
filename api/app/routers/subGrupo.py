from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from ..schemas.subGrupo import SubGrupoResponse
from ..models.SubGrupo import SubGrupoModel
from ..database import get_db

router = APIRouter(
    prefix="/subgrupo",
    tags=['SubGrupo']
)

@router.get("/", response_model=List[SubGrupoResponse])
def get_Sub_Grupo(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0):
    subGrupo = db.query(SubGrupoModel).all()
    return subGrupo

@router.get("/{id}", response_model=List[SubGrupoResponse])
def get_id(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(SubGrupoModel).filter(SubGrupoModel.grupo_id == id)

    subGrupo = post_query.all()

    if subGrupo == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"sub_grupo with grupo_id: {id} does not exist")
    return subGrupo