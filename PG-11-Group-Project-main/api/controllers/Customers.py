from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError




# Create Customer

def create_customer(db: Session, name: str, email: str, phone_number: str, address: str):
    new_customer = Customers()
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


# Read Customer
class Customer:
    pass


def read_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.customer_id == customer_id).first()


# Update Customer
def update_customer(db: Session, customer_id: int, name: str, email: str, phone_number: str, address: str):
    customer = read_customer(db, customer_id)
    if customer:
        customer.name = name
        customer.email = email
        customer.phone_number = phone_number
        customer.address = address
        db.commit()
        db.refresh(customer)
        return customer


# Delete Customer
def delete_customer(db: Session, customer_id: int):
    customer = read_customer(db, customer_id)
    if customer:
        db.delete(customer)
        db.commit()
        return customer
