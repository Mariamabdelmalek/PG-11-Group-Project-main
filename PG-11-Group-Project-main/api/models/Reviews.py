from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Reviews(Base):
    __tablename__ = 'reviews'

    review_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    menu_item_id = Column(Integer, ForeignKey('menu_items.menu_item_id'))
    review_text = Column(Text)
    score = Column(Integer)
