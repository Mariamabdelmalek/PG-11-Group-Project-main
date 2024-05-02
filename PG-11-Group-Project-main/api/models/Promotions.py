from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from sqlalchemy.orm import relationship
from . import Base
class Promotions(Base):
    __tablename__ = 'promotions'

    promotion_id = Column(Integer, primary_key=True, index=True)
    promotion_code = Column(String(50), index=True)
    expiration_date = Column(Date)
