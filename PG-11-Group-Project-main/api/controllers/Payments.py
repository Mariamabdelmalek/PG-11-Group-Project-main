from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..schemas.Payments import PaymentCreate, PaymentUpdate
from ..models.Payments import Payment


def get_payment(db: Session, payment_id: int):
    """Get a specific payment by ID."""
    payment = db.query(Payment).filter(Payment.payment_id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


def get_payments(db: Session):
    """Get all payments."""
    return db.query(Payment).all()


def create_payment(db: Session, payment: PaymentCreate):
    """Create a new payment."""
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


def update_payment(db: Session, payment_id: int, payment: PaymentUpdate):
    """Update an existing payment."""
    db_payment = get_payment(db, payment_id)
    for attr, value in payment.dict().items():
        setattr(db_payment, attr, value)
    db.commit()
    db.refresh(db_payment)
    return db_payment


def delete_payment(db: Session, payment_id: int):
    """Delete a payment."""
    db_payment = get_payment(db, payment_id)
    db.delete(db_payment)
    db.commit()
    return db_payment
