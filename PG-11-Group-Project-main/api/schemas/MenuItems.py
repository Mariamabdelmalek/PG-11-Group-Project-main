from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .MenuItems import MenuItems
class MenuItemBase(BaseModel):
    dish_name: str
    ingredients: str
    price: float
    calories: int
    food_category: str

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(MenuItemBase):
    pass

class MenuItemInDBBase(MenuItemBase):
    menu_item_id: int

    class Config:
        orm_mode = True

class MenuItem(MenuItemInDBBase):
    pass