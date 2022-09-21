"""
Repository abstraction implemented with sqlalchemy
Allows for better separation of concerns between the API services and the database logic
"""
import logging
from .models import EvDataPointRecord
from .database import SessionLocal

log = logging.getLogger(__name__)
db = SessionLocal()


def list_vehicle_data_points(
    limit,
    vehicle_id=None,
    from_timestamp=None,
    to_timestamp=None,
):
    """
    Retrieves vehicle data points from DB, filtering by vehicle_id and initial and final timestamps
    """

    # We need to confirm if 'vehicle_id' is a sensitive info before adding it to the log
    log.debug(
        "Retrieving vehicle data points - Timestamps: [%s - %s], Limit: %d",
        from_timestamp,
        to_timestamp,
        limit,
    )

    query = db.query(EvDataPointRecord)

    if vehicle_id:
        query = query.where(EvDataPointRecord.vehicle_id == vehicle_id)

    if from_timestamp:
        query = query.where(EvDataPointRecord.timestamp >= from_timestamp)
    if to_timestamp:
        query = query.where(EvDataPointRecord.timestamp <= to_timestamp)

    return query.limit(limit).all()


def get_vehicle_data_point(
    data_point_id: int,
):
    """
    Retrieves a single data point for a vehicle
    """
    query = db.query(EvDataPointRecord)
    row = query.get(data_point_id)
    return row


def save_vehicle_data_point(entry):
    """
    Saves a vehicle data point into the database
    """
    log.debug("Saving vehicle data point into DB")

    record = EvDataPointRecord(**entry.dict())
    db.add(record)
    db.commit()
