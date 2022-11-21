from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from ..schemas.rubro import RubroResponse, RubroCreate, RubroUpdate
from ..models.Rubro import RubroModel
from ..database import get_db

router = APIRouter(
    prefix="/rubro",
    tags=['Rubro']
)

@router.get("/", response_model=List[RubroResponse])
def get_Rubros(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0, nombre : Optional[str] = ""):
    rubro = db.query(RubroModel).filter(RubroModel.nombre.ilike(f'%{ nombre}%')).limit(limit).offset(offset).all()
    return rubro


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=RubroResponse)
def create_rubro(rubro: RubroCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_rubro = RubroModel(**rubro.dict())
    db.add(new_rubro)
    db.commit()
    db.refresh(new_rubro)

    return new_rubro

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rubro(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # HACE UNA CONSULTA A LA BASE DE DATOS PARA VER SI EXISTE
    post_query = db.query(RubroModel).filter(RubroModel.id == id)
    rubro = post_query.first()

    if rubro == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"rubro with id: {id} does not exist")
        
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=RubroResponse)
def update_post(id: int, updated_Rubro: RubroUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(RubroModel).filter(RubroModel.id == id)

    rubro = post_query.first()

    if rubro == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"rubro with id: {id} does not exist")
    
    update_data = updated_Rubro.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()

@router.get("/{id}", response_model=RubroResponse)
def get_id(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(RubroModel).filter(RubroModel.id == id)

    rubro = post_query.first()

    if rubro == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"rubro with id: {id} does not exist")
    return rubro