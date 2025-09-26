# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# USER SCHEMAS
class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    created_at: Optional[datetime]

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

    class Config:
        orm_mode = True


# RIDE SCHEMAS
class RideCreate(BaseModel):
    passenger_id: int                
    driver_id: Optional[int] = None
    pickup_location: str
    dropoff_location: str

class RideOut(BaseModel):
    id: int
    passenger_id: int
    driver_id: Optional[int] = None
    pickup_location: str
    dropoff_location: str
    status: Optional[str] = None
    requested_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    class Config:
        orm_mode = True
