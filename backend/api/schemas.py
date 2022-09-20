from datetime import datetime
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class ShiftStateEnum(str, Enum):
    DRIVE = "D"
    PARK = "P"
    REVERSE = "R"


class EvDataEntry(BaseModel):
    vehicle_id: int
    timestamp: datetime
    speed: Optional[int]
    odometer: Decimal
    soc: int
    elevation: int
    shift_state: Optional[ShiftStateEnum]

    def __init__(self, **data):
        if data["speed"] == "NULL":
            data.pop("speed")
        super().__init__(**data)

    @classmethod
    def from_orm(cls, obj):
        r = super().from_orm(obj)
        r.speed = r.speed or "NULL"
        return r

    class Config:
        orm_mode = True
