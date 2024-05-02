from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from pydantic import BaseModel


class Payment(Base):
    __tablename__ = 'Payments'

    payment_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('Customers.customer_id'))
    card_information = Column(String(255))
    transaction_status = Column(String(50))
    payment_type = Column(String(50))

    customer = relationship("Customer", back_populates="payments")