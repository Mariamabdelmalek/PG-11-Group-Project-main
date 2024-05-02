from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from pydantic import BaseModel

class MenuItem(Base):
    __tablename__ = 'MenuItems'

    menu_item_id = Column(Integer, primary_key=True)
    dish_name = Column(String(255))
    ingredients = Column(Text)
    price = Column(DECIMAL(10, 2))
    calories = Column(Integer)
    food_category = Column(String(100))