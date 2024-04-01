from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create(db: Session, sandwich: schemas.SandwichCreate):
    db_sandwich = models.Sandwich(
        name=sandwich.name,
        description=sandwich.description
    )
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwich_id, sandwich: schemas.SandwichUpdate):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich:
        for key, value in sandwich.dict(exclude_unset=True).items():
            setattr(db_sandwich, key, value)
        db.commit()
        db.refresh(db_sandwich)
    return db_sandwich

def delete(db: Session, sandwich_id):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich:
        db.delete(db_sandwich)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
