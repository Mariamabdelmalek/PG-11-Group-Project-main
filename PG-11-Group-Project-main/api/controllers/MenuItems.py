from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import MenuItems as models
from sqlalchemy.exc import SQLAlchemyError


def get_menu_item(db: Session, menu_item_id: int):
    """Get a specific menu item by ID."""
    menu_item = db.query(MenuItem).filter(MenuItem.menu_item_id == menu_item_id).first()
    if menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return menu_item


def get_menu_items(db: Session):
    """Get all menu items."""
    return db.query(MenuItem).all()


def create_menu_item(db: Session, menu_item: MenuItems.MenuItemCreate):
    """Create a new menu item."""
    db_menu_item = MenuItem(**menu_item.dict())
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item


def update_menu_item(db: Session, menu_item_id: int, menu_item: MenuItems.MenuItemUpdate):
    """Update an existing menu item."""
    db_menu_item = get_menu_item(db, menu_item_id)
    for attr, value in menu_item.dict().items():
        setattr(db_menu_item, attr, value)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item


def delete_menu_item(db: Session, menu_item_id: int):
    """Delete a menu item."""
    db_menu_item = get_menu_item(db, menu_item_id)
    db.delete(db_menu_item)
    db.commit()
    return db_menu_item
