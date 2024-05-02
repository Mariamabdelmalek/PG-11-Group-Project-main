from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .Payments import Payments


class PaymentBase(BaseModel):
    customer_id: int
    card_information: str
    transaction_status: str
    payment_type: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(PaymentBase):
    pass


class Payment(PaymentBase):
    payment_id: int

    class Config:
        orm_mode = True
