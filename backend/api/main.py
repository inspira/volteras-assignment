"""
Vehicle data API
"""
import logging
from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import EvDataPoint
from persistence import repository, schema
from config import API_DEFAULT_LISTING_LIMIT
from persistence.database import get_db, engine
from sqlalchemy.orm import Session

schema.Base.metadata.create_all(bind=engine)

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
    operation_id="list_vehicle_data_points",
)
async def list_vehicle_data_points(
    limit: int = API_DEFAULT_LISTING_LIMIT,
    db: Session = Depends(get_db)
):
    """
    Retrieves (GET) a list of generated data for a given vehicle_id, filtered by
    initial and final timestamps (optional). This endpoint should support pagination,
    sorting, and a way to limit the number of data returned.
    """
    return repository.list_vehicle_data_points(limit=limit, db=db)


@app.post(
    "/api/v1/vehicle_data/",
    status_code=status.HTTP_201_CREATED,
    tags=["evdata"],
    operation_id="post_vehicle_data_point",
)
async def post_vehicle_data_point(
    entry: EvDataPoint,
    db: Session = Depends(get_db),
):
    """
    Saves a data point for a vehicle in the database
    """
    repository.save_vehicle_data_point(entry=entry, db=db)
