from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from ..schemas.parametro import ParametroResponse, ParametroCreate, ParametroUpdate
from ..models.Parametro import ParametroModel
from ..database import get_db

router = APIRouter(
    prefix="/parametro",
    tags=['Parametro']
)

@router.get("/", response_model=List[ParametroResponse])
def get_Parametro(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0):
    parametro = db.query(ParametroModel).limit(limit).offset(offset).all()
    return parametro


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ParametroResponse)
def create_parametro(parametro: ParametroCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_parametro = ParametroModel(**parametro.dict())
    db.add(new_parametro)
    db.commit()
    db.refresh(new_parametro)

    return new_parametro

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_parametro(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # HACE UNA CONSULTA A LA BASE DE DATOS PARA VER SI EXISTE
    post_query = db.query(ParametroModel).filter(ParametroModel.id == id)
    parametro = post_query.first()

    if parametro == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"parametro with id: {id} does not exist")
        
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=ParametroResponse)
def update_post(id: int, updated_Parametro: ParametroUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(ParametroModel).filter(ParametroModel.id == id)

    parametro = post_query.first()

    if parametro == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"parametro with id: {id} does not exist")
    
    update_data = updated_Parametro.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()

@router.get("/{id}", response_model=ParametroResponse)
def get_id(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(ParametroModel).filter(ParametroModel.id == id)

    parametro = post_query.first()

    if parametro == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"parametro with id: {id} does not exist")
    return parametro