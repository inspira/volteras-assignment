"""
Vehicle data API
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import EvDataEntry

log = logging.getLogger(__name__)

app = FastAPI(
    title="Electric Vehicles Data",
    description="API over HTTP for Electric Vehicle data models management",
    version="1",
    openapi_tags=[{"name": "evdata"}],
)


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
  "/api/v1/vehicle_data",
  operation_id="list_vehicle_data_entries",
)
async def vehicle_data():
    """
    Retrieves (GET) a list of generated data for a given vehicle_id, filtered by
    initial and final timestamps (optional). This endpoint should support pagination,
    sorting, and a way to limit the number of data returned.
    """

    return [
              EvDataEntry(
                vehicle_id=1,
                timestamp='2022-07-12 16:42:25',
                speed="NULL",
                odometer=40800.6,
                soc=58,
                elevation=92,
                shift_state="NULL"
              ),
              EvDataEntry(
                vehicle_id=2,
                timestamp='2022-07-13 01:02:33',
                speed=37,
                odometer=47676.2,
                soc=73,
                elevation=4,
                shift_state="D"
              ),
            ]
