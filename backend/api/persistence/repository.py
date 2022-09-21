import logging
from .schema import EvDataPointRecord


log = logging.getLogger(__name__)


def list_vehicle_data_points(limit: int, db):
    log.debug("Retrieving vehicle data points from DB")

    query = db.query(EvDataPointRecord)
    return query.limit(limit).all()


def save_vehicle_data_point(entry, db):
    log.debug("Saving vehicle data point into DB")

    m = EvDataPointRecord(**entry.dict())
    db.add(m)
    db.commit()
