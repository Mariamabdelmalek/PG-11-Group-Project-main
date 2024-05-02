from fastapi import APIRouter, Depends, HTTPException, FastAPI, status, Response
from sqlalchemy.orm import Session
from typing import List
from ..schemas.Resources import Resource, ResourceCreate, ResourceUpdate
from ..controllers import Resources as controller
from ..schemas import orders as schema
from ..dependencies.database import get_db

router = APIRouter()


@router.get("/resources/{resource_id}", response_model=Resource)
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = controller.get_resource(db, resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource


@router.get("/resources/", response_model=List[Resource])
def read_resources(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    resources = controller.get_resources(db, skip=skip, limit=limit)
    return resources


@router.post("/resources/", response_model=Resource)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    return controller.create_resource(db=db, resource=resource)


@router.put("/resources/{resource_id}", response_model=Resource)
def update_resource(resource_id: int, resource: ResourceUpdate, db: Session = Depends(get_db)):
    return controller.update_resource(db=db, resource_id=resource_id, resource=resource)


@router.delete("/resources/{resource_id}", status_code=204)
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return controller.delete_resource(db=db, resource_id=resource_id)
