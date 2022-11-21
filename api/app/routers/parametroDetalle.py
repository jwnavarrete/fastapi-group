from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from ..models.ParametroDetalle import ParametroDetalleModel
from ..schemas.parametroDetalle import ParametroDetalleResponse, ParametroDetalleCreate, ParametroDetalleUpdate
from ..database import get_db
from ..Lib.general import modelDataExistById 
from ..models.ParametroDetalle import ParametroDetalleModel
# from ..models.Rubro import RubroModel
# from ..models.Tipo import TipoModel


router = APIRouter(
    prefix="/parametroDetalle",
    tags=['Parametro Detalle']
)

@router.get("/", response_model=List[ParametroDetalleResponse])
def get_ParametroDetalle(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0):
    parametroDetalle = db.query(ParametroDetalleModel).all()
    return parametroDetalle

@router.get("/{id}", response_model=ParametroDetalleResponse)
def get_id(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(ParametroDetalleModel).filter(ParametroDetalleModel.id == id)

    parametroDetalle = post_query.first()

    if parametroDetalle == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"parametro_detalle with id: {id} does not exist")
    return parametroDetalle



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ParametroDetalleResponse)
def create_parametroDetalle(parametro_detalle: ParametroDetalleCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_parametroDetalle = ParametroDetalleModel(**parametro_detalle.dict())
    db.add(new_parametroDetalle)
    db.commit()
    db.refresh(new_parametroDetalle)

    return new_parametroDetalle


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_parametroDetalle(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # HACE UNA CONSULTA A LA BASE DE DATOS PARA VER SI EXISTE
    post_query = db.query(ParametroDetalleModel).filter(ParametroDetalleModel.id == id)
    parametroDetalle = post_query.first()

    if parametroDetalle == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"parametro_detalle with id: {id} does not exist")
        
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=ParametroDetalleResponse)
def update_post(id: int, updated_ParametroDetalle: ParametroDetalleUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(ParametroDetalleModel).filter(ParametroDetalleModel.id == id)

    parametroDetalle = post_query.first()

    if parametroDetalle == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"parametro with id: {id} does not exist")
    
    update_data = updated_ParametroDetalle.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()