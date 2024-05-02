from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    customer_id: int
    menu_item_id: int
    review_text: str
    score: int


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[int] = None


class Review(ReviewBase):
    review_id: int

    class Config:
        orm_mode = True
