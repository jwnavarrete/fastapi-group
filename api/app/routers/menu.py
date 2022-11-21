from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from ..models.Menu import MenuModel
from ..schemas.menu import MenuResponse, MenuCreate, MenuUpdate, MenuParentResponse
from ..database import get_db
from ..Lib.general import modelDataExistById


router = APIRouter(
    prefix="/menu",
    tags=['Menu']
)

@router.get("/", response_model=List[MenuResponse])
# @router.get("/")
def get_all(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0, titulo : Optional[str] = ""):
    data = db.query(MenuModel).filter(MenuModel.titulo.contains(titulo)).limit(limit).offset(offset).all()
    return data


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MenuResponse)
def create(data: MenuCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # VALIDAMOS QUE EL MENU PADRE EXISTA
    if(data.parent_id == 0):
        data.parent_id = None
    
    if(data.parent_id):
        modelDataExistById(data.parent_id, db, 'Menu', MenuModel)

    new_data = MenuModel(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # HACE UNA CONSULTA A LA BASE DE DATOS PARA VER SI EXISTE
    post_query = db.query(MenuModel).filter(MenuModel.id == id)

    data = post_query.first()

    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Menu with id: {id} does not exist")
        
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=MenuResponse)
def update(id: int, updateParam: MenuUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # VALIDAMOS QUE EL MENU PADRE EXISTA
    # VALIDAMOS QUE EL MENU PADRE EXISTA
    if(updateParam.parent_id == 0):
        updateParam.parent_id = None
    
    if(updateParam.parent_id):
        modelDataExistById(updateParam.parent_id, db, 'Menu', MenuModel)

    post_query = db.query(MenuModel).filter(MenuModel.id == id)

    data = post_query.first()

    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Menu with id: {id} does not exist")
    
    update_data = updateParam.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()