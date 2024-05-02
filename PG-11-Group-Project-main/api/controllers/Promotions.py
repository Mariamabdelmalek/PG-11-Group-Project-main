from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import Promotions as model
from ..schemas import Promotions as schema
from ..dependencies.database import get_db
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()


@router.post("/promotions/", response_model=schema.Promotion)
def create_promotion(promotion: schema.PromotionCreate, db: Session = Depends(get_db)):
    db_promotion = model.Promotion(**promotion.dict())
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion


@router.get("/promotions/{promotion_id}", response_model=schema.Promotion)
def read_promotion(promotion_id: int, db: Session = Depends(get_db)):
    db_promotion = db.query(model.Promotion).filter(model.Promotion.promotion_id == promotion_id).first()
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return db_promotion


@router.put("/promotions/{promotion_id}", response_model=schema.Promotion)
def update_promotion(promotion_id: int, promotion: schema.PromotionUpdate, db: Session = Depends(get_db)):
    db_promotion = db.query(model.Promotion).filter(model.Promotion.promotion_id == promotion_id).first()
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    for key, value in promotion.dict().items():
        setattr(db_promotion, key, value)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion


@router.delete("/promotions/{promotion_id}", status_code=204)
def delete_promotion(promotion_id: int, db: Session = Depends(get_db)):
    db_promotion = db.query(model.Promotion).filter(model.Promotion.promotion_id == promotion_id).first()
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    db.delete(db_promotion)
    db.commit()
