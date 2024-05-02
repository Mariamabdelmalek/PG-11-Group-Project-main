from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from typing import List
from ..schemas.Promotions import Promotion, PromotionCreate, PromotionUpdate
from ..controllers import Promotions as controller
from ..schemas import Promotions as schema
from ..dependencies.database import get_db
from fastapi import APIRouter

router = APIRouter()


@router.get("/promotions/{promotion_id}", response_model=Promotion)
def read_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = controller.get_promotion(db, promotion_id)
    if promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion


@router.get("/promotions/", response_model=List[Promotion])
def read_promotions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    promotions = controller.get_promotions(db, skip=skip, limit=limit)
    return promotions


@router.post("/promotions/", response_model=Promotion)
def create_promotion(promotion: PromotionCreate, db: Session = Depends(get_db)):
    return controller.create_promotion(db=db, promotion=promotion)


@router.put("/promotions/{promotion_id}", response_model=Promotion)
def update_promotion(promotion_id: int, promotion: PromotionUpdate, db: Session = Depends(get_db)):
    return controller.update_promotion(db=db, promotion_id=promotion_id, promotion=promotion)


@router.delete("/promotions/{promotion_id}", status_code=204)
def delete_promotion(promotion_id: int, db: Session = Depends(get_db)):
    return controller.delete_promotion(db=db, promotion_id=promotion_id)
