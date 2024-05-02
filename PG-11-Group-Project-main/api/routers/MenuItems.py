from fastapi import APIRouter
from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import MenuItems as schema
from ..dependencies.database import engine, get_db

router = APIRouter()
# Example data for menu items
menu_items_db = [
    {
        "menu_item_id": 1,
        "dish_name": "Spaghetti Bolognese",
        "ingredients": "Spaghetti, ground beef, tomato sauce, onion, garlic",
        "price": 12.99,
        "calories": 750,
        "food_category": "Pasta"
    },
    {
        "menu_item_id": 2,
        "dish_name": "Caesar Salad",
        "ingredients": "Romaine lettuce, croutons, Parmesan cheese, Caesar dressing",
        "price": 8.99,
        "calories": 450,
        "food_category": "Salad"
    },
    # Add more example data as needed
]
@router.get("/menuitems/", response_model=List[MenuItems.MenuItem])
async def get_menu_items():
    """Get all menu items."""
    return menu_items_db

@router.get("/menuitems/{menu_item_id}", response_model=MenuItems.MenuItem)
async def get_menu_item(menu_item_id: int):
    """Get a specific menu item by ID."""
    for item in menu_items_db:
        if item["menu_item_id"] == menu_item_id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

@router.post("/menuitems/", response_model=MenuItems.MenuItem)
async def create_menu_item(menu_item: MenuItems.MenuItemCreate):
    """Create a new menu item."""
    menu_item_id = max(item["menu_item_id"] for item in menu_items_db) + 1
    menu_item_dict = menu_item.dict()
    menu_item_dict["menu_item_id"] = menu_item_id
    menu_items_db.append(menu_item_dict)
    return menu_item_dict