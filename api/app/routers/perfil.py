from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func
from .. import oauth2
from ..schemas.perfil import PerfilResponse, PerfilCreate, PerfilUpdate
from ..models.Perfil import PerfilModel
from ..database import get_db

router = APIRouter(
    prefix="/perfiles",
    tags=['Perfiles']
)

@router.get("/", response_model=List[PerfilResponse])
def get_perfiles(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0, search : Optional[str] = ""):
    perfiles = db.query(PerfilModel).filter(PerfilModel.descripcion.ilike(f'%{ search}%')).limit(limit).offset(offset).all()
    return perfiles


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PerfilResponse)
def create_perfiles(perfil: PerfilCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_perfil = PerfilModel(**perfil.dict())
    db.add(new_perfil)
    db.commit()
    db.refresh(new_perfil)

    return new_perfil

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_perfil(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(PerfilModel).filter(PerfilModel.id == id)

    perfil = post_query.first()

    if perfil == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"perfil with id: {id} does not exist")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=PerfilResponse)
def update_post(id: int, updated_perfil: PerfilUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(PerfilModel).filter(PerfilModel.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    update_data = updated_perfil.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()