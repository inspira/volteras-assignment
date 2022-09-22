# -*- coding: utf-8 -*-
"""
API Models using pydantic syntax
"""
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
# pylint: disable=no-name-in-module
from typing import Optional
from pydantic import BaseModel


class ShiftStateEnum(str, Enum):
    """
    Represents the possible values for the shift state of an EV
    """
    NULL = 'NULL'
    DRIVE = 'D'
    PARK = 'P'
    REVERSE = 'R'


@dataclass
class EvDataEntry(BaseModel):
    """
    Represents a data entry for a given vehicle_id
    """
    vehicle_id: str
    timestamp: datetime
    speed: Optional[int]
    odometer: Decimal
    soc: int
    elevation: int
    shift_state: ShiftStateEnum

    def __init__(self, **data):
        """
        Save speed as a nullable integer in the DB
        so we can make calculations on them
        """
        if data['speed'] == 'NULL':
            data.pop('speed')
        super().__init__(**data)

    @classmethod
    def from_orm(cls, obj):
        """
        Retrieves a NULL value from DB and sets it as string
        """
        row = super().from_orm(obj)
        row.speed = row.speed or 'NULL'
        return row

    @dataclass
    class Config:
        """
        Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict,
        but an ORM model (or any other arbitrary object with attributes).
        See: https://fastapi.tiangolo.com/tutorial/sql-databases/
        """
        orm_mode = True
