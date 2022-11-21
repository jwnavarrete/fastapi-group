from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from ..models.MenuPerfil import MenuPerfilModel
from ..schemas.menuPerfil import MenuPerfilResponse, MenuPerfilCreate, MenuPerfilUpdate
from ..database import get_db
from ..Lib.general import modelDataExistById 
from ..models.Perfil import PerfilModel
from ..models.Menu import MenuModel

router = APIRouter(
    prefix="/menu-perfil",
    tags=['Menu Perfil']
)

@router.get("/", response_model=List[MenuPerfilResponse])
def get_all(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0):
    data = db.query(MenuPerfilModel).limit(limit).offset(offset).all()
    return data

@router.get("/{id}", response_model=MenuPerfilResponse)
def get_one(perfil_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0):
    data = db.query(MenuPerfilModel).filter(MenuPerfilModel.perfil_id == perfil_id).limit(limit).offset(offset).first()
    return data


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MenuPerfilResponse)
def create(data: MenuPerfilCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_data = MenuPerfilModel(**data.dict())
    # 
    modelDataExistById(data.perfil_id, db, 'Perfil', PerfilModel)
    modelDataExistById(data.menu_id, db, 'Menu', MenuModel)

    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(perfil_id: int, menu_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # HACE UNA CONSULTA A LA BASE DE DATOS PARA VER SI EXISTE
    post_query = db.query(MenuPerfilModel).filter(MenuPerfilModel.perfil_id == perfil_id).filter(MenuPerfilModel.menu_id == menu_id)

    data = post_query.first()

    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Menu Perfil with id: {id} does not exist")
        
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=MenuPerfilResponse)
def update(perfil_id: int, menu_id: int, updateParam: MenuPerfilUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(MenuPerfilModel).filter(MenuPerfilModel.perfil_id == perfil_id).filter(MenuPerfilModel.menu_id == menu_id)

    data = post_query.first()

    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Menu Perfil with id: {id} does not exist")
    
    update_data = updateParam.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()