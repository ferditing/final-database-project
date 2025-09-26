from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(30), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    rides = relationship("Ride", back_populates="passenger")

class Ride(Base):
    __tablename__ = "rides"
    id = Column(Integer, primary_key=True, index=True)
    passenger_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    driver_id = Column(Integer, nullable=True)
    pickup_location = Column(String(255), nullable=False)
    dropoff_location = Column(String(255), nullable=False)
    status = Column(String(30), nullable=False, server_default="requested")
    requested_at = Column(DateTime, server_default=func.now())
    completed_at = Column(DateTime, nullable=True)

    passenger = relationship("User", back_populates="rides")
