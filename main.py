# main.py
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Uber-like API (Assignment)")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# USERS

# Create a user
@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Get all users
@app.get("/users/", response_model=List[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)

# Get single user by id
@app.get("/users/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Update user (partial update allowed)
@app.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user_endpoint(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = crud.update_user(db=db, user_id=user_id, user_update=user_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

# Delete user
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db=db, user_id=user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    # 204 No Content — successful deletion with no body
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# RIDES

# Create a ride
@app.post("/rides/", response_model=schemas.RideOut)
def create_ride(ride: schemas.RideCreate, db: Session = Depends(get_db)):
    passenger = crud.get_user(db=db, user_id=ride.passenger_id)
    if passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return crud.create_ride(db=db, ride=ride)

# Get all rides
@app.get("/rides/", response_model=List[schemas.RideOut])
def read_rides(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_rides(db=db, skip=skip, limit=limit)

# Get single ride by id
@app.get("/rides/{ride_id}", response_model=schemas.RideOut)
def read_ride(ride_id: int, db: Session = Depends(get_db)):
    db_ride = crud.get_ride(db=db, ride_id=ride_id)
    if db_ride is None:
        raise HTTPException(status_code=404, detail="Ride not found")
    return db_ride
