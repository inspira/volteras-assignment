import logging
from .models import EvDataPointRecord
from .database import SessionLocal

log = logging.getLogger(__name__)
db = SessionLocal()


def list_vehicle_data_points(limit: int):
    log.debug("Retrieving vehicle data points from DB")

    query = db.query(EvDataPointRecord)
    return query.limit(limit).all()


def save_vehicle_data_point(entry):
    log.debug("Saving vehicle data point into DB")

    m = EvDataPointRecord(**entry.dict())
    db.add(m)
    db.commit()
