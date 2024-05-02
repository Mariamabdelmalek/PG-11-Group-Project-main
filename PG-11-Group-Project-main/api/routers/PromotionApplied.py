from fastapi import APIRouter
from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import PromotionApplied as controller
from ..schemas import PromotionApplied as schema
from ..dependencies.database import engine, get_db

router = APIRouter()


@router.post("/promotion_applied/", response_model=PromotionApplied)
def create_promotion_applied(promotion_applied: PromotionAppliedCreate, db: Session = Depends(get_db)):
    """Create a new promotion applied."""
    return create_promotion_applied(db, promotion_applied)
