# -*- coding: utf-8 -*-
"""
Repository abstraction implemented with sqlalchemy
Allows for better separation of concerns between the API services and the database logic
"""
import logging
from sqlalchemy import desc
from sqlalchemy.orm import Session
from .models import EvDataPointRecord
from .repository import Repository

log = logging.getLogger(__name__)


class SqlAlchemyRepository(Repository):
    """
    Implementation of the repository pattern for SQL Alchemy
    """

    db_session: Session = None

    def __init__(self, db_session_arg):
        self.db_session = db_session_arg
        super()

    # pylint: disable=too-many-arguments
    def list_vehicle_data_points(
        self,
        vehicle_id=None,
        from_timestamp=None,
        to_timestamp=None,
        sort_by=None,
        sort_order=None,
        page_size=None,
        page_index=None
    ):
        """
        Retrieves vehicle data points from DB, filtering by
        vehicle_id and initial and final timestamps
        """

        # We need to confirm if 'vehicle_id' is a sensitive info before adding it to the log
        log.debug(
            'Retrieving vehicle data points - Timestamps: [%s - %s], Paging: %s %s, Sort %s %s',
            from_timestamp,
            to_timestamp,
            page_size,
            page_index,
            sort_by,
            sort_order,
        )

        try:
            query = self.db_session.query(EvDataPointRecord)

            if vehicle_id:
                query = query.where(EvDataPointRecord.vehicle_id == vehicle_id)

            if from_timestamp:
                query = query.where(EvDataPointRecord.timestamp >= from_timestamp)
            if to_timestamp:
                query = query.where(EvDataPointRecord.timestamp <= to_timestamp)

            total_items = query.count()

            # Check if sort column exists in the DB schema before sorting
            if sort_by and hasattr(EvDataPointRecord, sort_by):
                if sort_order and sort_order.lower() == 'desc':
                    query = query.order_by(desc(sort_by))
                else:
                    query = query.order_by(sort_by)

            if page_size and page_index and page_size >= 0 and page_index > 0:
                query = query.offset((page_index - 1) * page_size).limit(page_size)

            data = query.all()
            return (data, total_items)
        except Exception as exc:
            log.error('Database exception when listing data points: %s', exc)
            # self.db_session.rollback()
            raise


    def get_vehicle_data_point(
        self,
        data_point_id: int,
    ):
        """
        Retrieves a single data point for a vehicle
        """
        try:
            query = self.db_session.query(EvDataPointRecord)
            row = query.get(data_point_id)
            return row
        except Exception as exc:
            log.error('Database exception when getting data point: %s', exc)
            # self.db_session.rollback()
            raise


    def save_vehicle_data_point(
        self,
        entry,
    ):
        """
        Saves a vehicle data point into the database
        """
        log.debug('Saving vehicle data point into DB')

        record = EvDataPointRecord(**entry.dict())
        try:
            self.db_session.add(record)
            self.db_session.commit()
        except Exception as exc:
            log.error('Database exception when saving data point: %s', exc)
            # self.db_session.rollback()
            raise
