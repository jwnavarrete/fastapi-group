from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import utils, oauth2
from ..schemas.auth import Token
from ..models.User import UserModel
from ..database import get_db


router = APIRouter(
    prefix="/auth",
    tags=['Authentication']
)

@router.post('/login', response_model=Token)
def login(user_credentials:  OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == user_credentials.username).filter(UserModel.estado == 'A').first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    # create a token 
    # return tokrn 

    access_token = oauth2.create_access_token(data = {"user_id" : user.id})
    return {"access_token" : access_token, "token_type" : "bearer"}


