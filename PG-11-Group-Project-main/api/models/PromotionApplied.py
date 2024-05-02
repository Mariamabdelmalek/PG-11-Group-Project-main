from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from . import Base
from ..dependencies.database import Base
from pydantic import BaseModel

class PromotionApplied(Base):
    __tablename__ = 'promotion_applied'

    promotion_id = Column(Integer, ForeignKey('promotions.promotion_id'), primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    menu_item_id = Column(Integer, ForeignKey('menu_items.menu_item_id'), primary_key=True)

    promotion = relationship("Promotion")
    order = relationship("Order")
    menu_item = relationship("MenuItem")
