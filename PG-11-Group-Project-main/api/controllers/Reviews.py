from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models.Reviews import Reviews
from ..schemas.Reviews import ReviewCreate, ReviewUpdate
from sqlalchemy.exc import SQLAlchemyError


def get_review(db: Session, review_id: int):
    return db.query(Reviews).filter(Reviews.review_id == review_id).first()


def get_reviews(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Reviews).offset(skip).limit(limit).all()


def create_review(db: Session, review: ReviewCreate):
    db_review = Reviews(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def update_review(db: Session, review_id: int, review: ReviewUpdate):
    db_review = db.query(Reviews).filter(Reviews.review_id == review_id).first()
    for key, value in review.dict().items():
        setattr(db_review, key, value)
    db.commit()
    db.refresh(db_review)
    return db_review


def delete_review(db: Session, review_id: int):
    db_review = db.query(Reviews).filter(Reviews.review_id == review_id).first()
    db.delete(db_review)
    db.commit()
