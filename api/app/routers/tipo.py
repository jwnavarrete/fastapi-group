from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from ..schemas.tipo import TipoResponse, TipoCreate, TipoUpdate
from ..models.Tipo import TipoModel
from ..database import get_db

router = APIRouter(
    prefix="/tipo",
    tags=['Tipo']
)

@router.get("/", response_model=List[TipoResponse])
def get_tipos(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0, nombre : Optional[str] = ""):
    tipos = db.query(TipoModel).filter(TipoModel.nombre.ilike(f'%{ nombre}%')).limit(limit).offset(offset).all()
    return tipos


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TipoResponse)
def create_tipo(tipo: TipoCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_tipo = TipoModel(**tipo.dict())
    db.add(new_tipo)
    db.commit()
    db.refresh(new_tipo)

    return new_tipo

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tipo(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # HACE UNA CONSULTA A LA BASE DE DATOS PARA VER SI EXISTE
    post_query = db.query(TipoModel).filter(TipoModel.id == id)
    tipo = post_query.first()

    if tipo == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"tipo with id: {id} does not exist")
        
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=TipoResponse)
def update_post(id: int, updated_Tipo: TipoUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(TipoModel).filter(TipoModel.id == id)

    tipo = post_query.first()

    if tipo == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"tipo with id: {id} does not exist")
    
    update_data = updated_Tipo.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()

@router.get("/{id}", response_model=TipoResponse)
def get_id(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(TipoModel).filter(TipoModel.id == id)

    tipo = post_query.first()

    if tipo == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"tipo with id: {id} does not exist")
    return tipo