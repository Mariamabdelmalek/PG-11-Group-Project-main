from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas.Reviews import Review, ReviewCreate, ReviewUpdate
from ..controllers import Reviews as controller
from ..dependencies.database import get_db

router = APIRouter()


@router.get("/reviews/{review_id}", response_model=Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    review = controller.get_review(db, review_id)
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review


@router.get("/reviews/", response_model=List[Review])
def read_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reviews = controller.get_reviews(db, skip=skip, limit=limit)
    return reviews


@router.post("/reviews/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return controller.create_review(db=db, review=review)


@router.put("/reviews/{review_id}", response_model=Review)
def update_review(review_id: int, review: ReviewUpdate, db: Session = Depends(get_db)):
    return controller.update_review(db=db, review_id=review_id, review=review)


@router.delete("/reviews/{review_id}", status_code=204)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    return controller.delete_review(db=db, review_id=review_id)
