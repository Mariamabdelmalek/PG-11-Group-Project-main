from fastapi import APIRouter
from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import Customers as schema
from ..dependencies.database import engine, get_db



router = APIRouter()

@router.get("/customers/")
def get_customers():
    # Logic to retrieve customers from the database
    return {"message": "List of customers"}

@router.post("/customers/")
def create_customer():
    # Logic to create a new customer
    return {"message": "Customer created successfully"}