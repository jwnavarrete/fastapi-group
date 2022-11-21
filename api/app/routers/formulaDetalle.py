from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from ..models.FormulaDetalle import FormulaDetalleModel
from ..schemas.formulaDetalle import FormulaDetalleResponse, FormulaDetalleCreate, FormulaDetalleUpdate
from ..database import get_db
from ..Lib.general import modelDataExistById 
from ..models.Formula import FormulaModel
from ..models.Rubro import RubroModel
from ..models.Tipo import TipoModel


router = APIRouter(
    prefix="/formula-det",
    tags=['Formula Detalle']
)

@router.get("/", response_model=List[FormulaDetalleResponse])
def get_formulas(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0, valor : Optional[str] = ""):
    formulas = db.query(FormulaDetalleModel).filter(FormulaDetalleModel.valor.ilike(f'%{ valor}%')).limit(limit).offset(offset).all()
    return formulas

@router.get("/{id}", response_model=List[FormulaDetalleResponse])
def get_All_By_FormulaId(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = db.query(FormulaDetalleModel).filter(FormulaDetalleModel.formula_id == id).all()

    return data


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FormulaDetalleResponse)
def create_formula(formula: FormulaDetalleCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # validamos que los campos relacion sean validos
    modelDataExistById(formula.formula_id, db, 'Formula', FormulaModel)
    modelDataExistById(formula.rubro_id, db, 'Rubro', RubroModel)
    modelDataExistById(formula.tipo_id, db, 'Tipo', TipoModel)

    new_formula = FormulaDetalleModel(**formula.dict())
    db.add(new_formula)
    db.commit()
    db.refresh(new_formula)

    return new_formula

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_formula(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # HACE UNA CONSULTA A LA BASE DE DATOS PARA VER SI EXISTE
    post_query = db.query(FormulaDetalleModel).filter(FormulaDetalleModel.id == id)

    formula = post_query.first()

    if formula == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"formula detail with id: {id} does not exist")
        
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=FormulaDetalleResponse)
def update_post(id: int, updated_formula: FormulaDetalleUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # validamos que los campos relacion sean validos
    modelDataExistById(updated_formula.formula_id, db, 'Formula', FormulaModel)
    modelDataExistById(updated_formula.rubro_id, db, 'Rubro', RubroModel)
    modelDataExistById(updated_formula.tipo_id, db, 'Tipo', TipoModel)
    # 
    post_query = db.query(FormulaDetalleModel).filter(FormulaDetalleModel.id == id)

    formula = post_query.first()

    if formula == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"formula detail with id: {id} does not exist")
    
    update_data = updated_formula.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()