"""
Vehicle data API
"""
import logging
from datetime import datetime
from typing import Optional
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from config import API_DEFAULT_LISTING_LIMIT, ALLOWED_ORIGINS
from models import EvDataEntry
from persistence import repository


log = logging.getLogger(__name__)

app = FastAPI(
    title="Electric Vehicles Data",
    description="API over HTTP for Electric Vehicle data models management",
    version="1",
    openapi_tags=[{"name": "evdata"}],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/api/v1/vehicle_data/{data_point_id}",
    operation_id="get_single_vehicle_data_point",
)
async def get_single_vehicle_data_point(
    data_point_id: int,
):
    """
    Reads a single data point from the database, given its id
    """
    return repository.get_vehicle_data_point(
        data_point_id=data_point_id
    )


@app.get(
    "/api/v1/vehicle_data/",
    operation_id="list_vehicle_data_points",
)
async def list_vehicle_data_points(
    vehicle_id: Optional[str] = None,
    from_timestamp: Optional[datetime] = None,
    to_timestamp: Optional[datetime] = None,
    limit: int = API_DEFAULT_LISTING_LIMIT,
):
    """
    Retrieves a list of generated data for a given vehicle_id, filtered by
    initial and final timestamps (optional). This endpoint should support pagination,
    sorting, and a way to limit the number of data returned.
    """
    return repository.list_vehicle_data_points(
        vehicle_id=vehicle_id,
        from_timestamp=from_timestamp,
        to_timestamp=to_timestamp,
        limit=limit
    )


@app.post(
    "/api/v1/vehicle_data/",
    status_code=status.HTTP_201_CREATED,
    tags=["evdata"],
    operation_id="post_vehicle_data_point",
)
async def post_vehicle_data_point(
    entry: EvDataEntry,
):
    """
    Saves a data point for a vehicle in the database
    """
    repository.save_vehicle_data_point(entry=entry)


@app.get("/health", operation_id="health")
def health() -> str:
    """
    Performs a quick health check
    """
    repository.list_vehicle_data_points(
        vehicle_id=None,
        limit=0,
    )
    return "OK"
