from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends, APIRouter
from ..models import PromotionApplied
from ..database import get_db
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()


@router.post("/promotion_applied/")
def create_promotion_applied(promotion_applied: PromotionAppliedCreate, db: Session = Depends(get_db)):
    db_promotion_applied = PromotionApplied
    db.add(db_promotion_applied)
    db.commit()
    db.refresh(db_promotion_applied)
    return db_promotion_applied


@router.get("/promotion_applied/{promotion_applied_id}", response_model=schema.PromotionApplied)
def read_promotion_applied(promotion_applied_id: int, db: Session = Depends(get_db)):
    db_promotion_applied = db.query(model.PromotionApplied).filter(
        model.PromotionApplied.id == promotion_applied_id).first()
    if db_promotion_applied is None:
        raise HTTPException(status_code=404, detail="PromotionApplied not found")
    return db_promotion_applied


@router.put("/promotion_applied/{promotion_applied_id}", response_model=schema.PromotionApplied)
def update_promotion_applied(promotion_applied_id: int, promotion_applied: schema.PromotionAppliedUpdate,
                             db: Session = Depends(get_db)):
    db_promotion_applied = db.query(model.PromotionApplied).filter(
        model.PromotionApplied.id == promotion_applied_id).first()
    if db_promotion_applied is None:
        raise HTTPException(status_code=404, detail="PromotionApplied not found")
    for key, value in promotion_applied.dict().items():
        setattr(db_promotion_applied, key, value)
    db.commit()
    db.refresh(db_promotion_applied)
    return db_promotion_applied


@router.delete("/promotion_applied/{promotion_applied_id}", status_code=204)
def delete_promotion_applied(promotion_applied_id: int, db: Session = Depends(get_db)):
    db_promotion_applied = db.query(model.PromotionApplied).filter(
        model.PromotionApplied.id == promotion_applied_id).first()
    if db_promotion_applied is None:
        raise HTTPException(status_code=404, detail="PromotionApplied not found")
    db.delete(db_promotion_applied)
    db.commit()
