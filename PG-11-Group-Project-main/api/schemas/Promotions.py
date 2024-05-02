from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .Promotions import Promotions


class PromotionBase(BaseModel):
    promotion_code: str
    expiration_date: date


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(PromotionBase):
    pass


class Promotion(PromotionBase):
    promotion_id: int

    class Config:
        orm_mode = True
