from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from pydantic import BaseModel


class Customer(Base):
    __tablename__ = 'Customers'
    customer_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    phone_number = Column(String(20))
    address = Column(String(255))
