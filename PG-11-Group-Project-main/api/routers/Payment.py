from fastapi import APIRouter
from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import Payments as controller
from ..schemas import Payments as schema
from ..dependencies.database import engine, get_db

router = APIRouter()


@router.get("/payments/", response_model=list[Payment])
def read_payments(db: Session = Depends(get_db)):
    """Get all payments."""
    return get_payments(db)


@router.get("/payments/{payment_id}", response_model=Payment)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    """Get a specific payment by ID."""
    return get_payment(db, payment_id)


@router.post("/payments/", response_model=Payment)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    """Create a new payment."""
    return create_payment(db, payment)


@router.put("/payments/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, payment: PaymentUpdate, db: Session = Depends(get_db)):
    """Update an existing payment."""
    return update_payment(db, payment_id, payment)


@router.delete("/payments/{payment_id}", response_model=Payment)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    """Delete a payment."""
    return delete_payment(db, payment_id)
