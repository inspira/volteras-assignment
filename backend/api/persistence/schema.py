from sqlalchemy import Column, Integer, String, DateTime, Float
from .database import Base


class EvDataPointRecord(Base):
    __tablename__ = "ev_data_points"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(36), index=True)
    timestamp = Column(DateTime)
    speed = Column(Integer, nullable=True)
    odometer = Column(Float)
    soc = Column(Integer)
    elevation = Column(Integer)
    shift_state = Column(String(4))
