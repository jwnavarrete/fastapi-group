from fastapi import status, HTTPException
from sqlalchemy.orm import Session

def modelDataExistById(id:int, db: Session, campo: str, Model):
    data = db.query(Model).filter(Model.id == id).first()
    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{campo} with id: {id} does not exist")
