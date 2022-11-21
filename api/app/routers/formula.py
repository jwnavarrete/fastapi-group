from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from ..models.Formula import FormulaModel
from ..schemas.formula import FormulaResponse, FormulaCreate, FormulaUpdate
from ..database import get_db

router = APIRouter(
    prefix="/formula",
    tags=['Formula']
)

@router.get("/", response_model=List[FormulaResponse])
def get_formulas(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0, version : Optional[str] = ""):
    formulas = db.query(FormulaModel).filter(FormulaModel.version.ilike(f'%{ version}%') ).limit(limit).offset(offset).all()
    return formulas

@router.get("/{id}", response_model=FormulaResponse)
def getOne(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(FormulaModel).filter(FormulaModel.id == id)

    formula = post_query.first()

    if formula == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"formula with id: {id} does not exist")
            
    return formula


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FormulaResponse)
def create_formula(formula: FormulaCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_formula = FormulaModel(user_id=current_user.id, **formula.dict())
    db.add(new_formula)
    db.commit()
    db.refresh(new_formula)

    return new_formula

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_formula(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # HACE UNA CONSULTA A LA BASE DE DATOS PARA VER SI EXISTE
    post_query = db.query(FormulaModel).filter(FormulaModel.id == id)

    formula = post_query.first()

    if formula == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"formula with id: {id} does not exist")
        
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=FormulaResponse)
def update_post(id: int, updated_formula: FormulaUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(FormulaModel).filter(FormulaModel.id == id)

    formula = post_query.first()

    if formula == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"formula with id: {id} does not exist")
    
    update_data = updated_formula.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()