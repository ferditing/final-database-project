# crud.py
from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

# Users
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email or phone already exists")
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None

    # apply only fields provided
    update_data = user_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)

    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        # duplicate email or phone
        raise HTTPException(status_code=400, detail="Email or phone already exists")
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        return False
    db.delete(db_user)
    db.commit()
    return True



# Rides
def create_ride(db: Session, ride: schemas.RideCreate):
    db_ride = models.Ride(
        passenger_id=ride.passenger_id,
        driver_id=ride.driver_id,
        pickup_location=ride.pickup_location,
        dropoff_location=ride.dropoff_location,
        status="requested"
    )
    db.add(db_ride)
    db.commit()
    db.refresh(db_ride)
    return db_ride

def get_ride(db: Session, ride_id: int):
    return db.query(models.Ride).filter(models.Ride.id == ride_id).first()

def get_rides(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ride).offset(skip).limit(limit).all()

def complete_ride(db: Session, ride_id: int):
    ride = get_ride(db, ride_id)
    if not ride:
        return None
    ride.status = "completed"
    from sqlalchemy.sql import func
    ride.completed_at = func.now()
    db.commit()
    db.refresh(ride)
    return ride
