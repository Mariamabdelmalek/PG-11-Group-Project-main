from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..schemas.Resources import ResourceCreate, ResourceUpdate
from ..models import Resources as model
from sqlalchemy.exc import SQLAlchemyError


def get_resource(db: Session, resource_id: int):
    return db.query(Resources).filter(Resources.resource_id == resource_id).first()


def get_resources(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Resources).offset(skip).limit(limit).all()


def create_resource(db: Session, resource: ResourceCreate):
    db_resource = Resources(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource


def update_resource(db: Session, resource_id: int, resource: ResourceUpdate):
    db_resource = db.query(Resources).filter(Resources.resource_id == resource_id).first()
    for key, value in resource.dict().items():
        setattr(db_resource, key, value)
    db.commit()
    db.refresh(db_resource)
    return db_resource


def delete_resource(db: Session, resource_id: int):
    db_resource = db.query(Resources).filter(Resources.resource_id == resource_id).first()
    db.delete(db_resource)
    db.commit()
