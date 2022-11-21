from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from .. import utils
from ..schemas.user import UserResponse, UserCreate, UserLogin, UserUpdate
from ..models.User import UserModel
from ..models.Perfil import PerfilModel
from ..database import get_db
from ..Lib.general import modelDataExistById

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), search : Optional[str] = ""):
    users = db.query(UserModel).filter(UserModel.email.ilike(f'%{ search}%')).all()
    return users

@router.get('/{id}', response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db), ):
    data = db.query(UserModel).filter(UserModel.id == id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")
    return data


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # hash the password - user.password
    modelDataExistById(user.perfil_id, db, 'Perfil', PerfilModel)
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.patch("/{id}", response_model=UserResponse)
def update_post(id: int, userUpdate: UserUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    hashed_password = utils.hash(userUpdate.password)
    userUpdate.password = hashed_password

    modelDataExistById(userUpdate.perfil_id, db, 'Perfil', PerfilModel)
    post_query = db.query(UserModel).filter(UserModel.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    update_data = userUpdate.dict(exclude_unset=True)

    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(UserModel).filter(UserModel.id == id)

    perfil = post_query.first()

    if perfil == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Usuario with id: {id} does not exist")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)