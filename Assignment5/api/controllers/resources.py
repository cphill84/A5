from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import models, schemas

def create_resource(db: Session, resource: schemas.ResourceCreate):
    db_resource = models.Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def get_all_resources(db: Session):
    return db.query(models.Resource).all()

def get_resource(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update_resource(db: Session, resource_id: int, resource: schemas.ResourceUpdate):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    for key, value in resource.dict(exclude_unset=True).items():
        setattr(db_resource, key, value)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def delete_resource(db: Session, resource_id: int):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(db_resource)
    db.commit()
    return {"message": "Resource deleted successfully"}
