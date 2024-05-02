from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .PromotionApplied import PromotionApplied

class PromotionAppliedBase(BaseModel):
    promotion_id: int
    order_id: int
    menu_item_id: int


class PromotionAppliedCreate(PromotionAppliedBase):
    pass


class PromotionAppliedUpdate(PromotionAppliedBase):
    pass


class PromotionApplied(PromotionAppliedBase):
    class Config:
        orm_mode = True
