from pydantic import BaseModel
from .formula import FormulaResponse
from .rubro import RubroResponse
from .tipo import TipoResponse

class FormulaDetalleCreate(BaseModel): 
    orden: int
    valor : str
    visible: bool
    formula_id: int
    rubro_id: int
    tipo_id: int
    
class FormulaDetalleUpdate(BaseModel): 
    orden: int
    valor : str
    visible: bool
    formula_id: int
    rubro_id: int
    tipo_id: int
    
class FormulaDetalleResponse(FormulaDetalleCreate):
    id: int
    formula: FormulaResponse
    rubro: RubroResponse
    tipo: TipoResponse

    class Config:
        orm_mode = True