from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import models, schemas

def create_order_detail(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_detail = models.OrderDetail(**order_detail.dict())
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def get_all_order_details(db: Session):
    return db.query(models.OrderDetail).all()

def get_order_detail(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update_order_detail(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if not db_order_detail:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    for key, value in order_detail.dict(exclude_unset=True).items():
        setattr(db_order_detail, key, value)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def delete_order_detail(db: Session, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if not db_order_detail:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    db.delete(db_order_detail)
    db.commit()
    return {"message": "Order Detail deleted successfully"}
