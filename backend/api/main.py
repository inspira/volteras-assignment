# -*- coding: utf-8 -*-
"""
Vehicle data API
"""
import logging
from typing import Optional
from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware

from config import API_DEFAULT_LISTING_LIMIT, ALLOWED_ORIGINS
from models import EvDataEntry, EvDataEntryPaginatedResponse
from persistence.repository import Repository
from persistence import get_repository
from persistence.database import init_db

init_db()

log = logging.getLogger(__name__)

app = FastAPI(
    title='Electric Vehicles Data',
    description='API over HTTP for Electric Vehicle data models management',
    version='1',
    openapi_tags=[{'name': 'evdata'}],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=list(ALLOWED_ORIGINS),
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get(
    '/api/v1/vehicle_data/{data_point_id}',
    operation_id='get_single_vehicle_data_point',
)
async def get_single_vehicle_data_point(
    data_point_id: int,
    repo: Repository = Depends(get_repository),
):
    """
    Reads a single data point from the database, given its id
    """
    return repo.get_vehicle_data_point(
        data_point_id=data_point_id
    )


@app.get(
    '/api/v1/vehicle_data/',
    response_model=EvDataEntryPaginatedResponse,
    operation_id='list_vehicle_data_points',
)
# pylint: disable=too-many-arguments
async def list_vehicle_data_points(
    vehicle_id: Optional[str] = None,
    from_timestamp: Optional[str] = None,
    to_timestamp: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = None,
    page_size: Optional[int] = API_DEFAULT_LISTING_LIMIT,
    page_index: Optional[int] = 1,
    repo: Repository = Depends(get_repository),
):
    """
    Retrieves a list of generated data for a given vehicle_id, filtered by
    initial and final timestamps (optional). This endpoint should support pagination,
    sorting, and a way to limit the number of data returned.
    """
    (data, total_items) = repo.list_vehicle_data_points(
        vehicle_id=vehicle_id,
        from_timestamp=from_timestamp,
        to_timestamp=to_timestamp,
        sort_by=sort_by,
        sort_order=sort_order,
        page_size=page_size,
        page_index=page_index,
    )

    return {
        'page_index': page_index,
        'page_size': page_size,
        'total_items': total_items,
        'data': data,
    }


@app.post(
    '/api/v1/vehicle_data/',
    status_code=status.HTTP_201_CREATED,
    tags=['evdata'],
    operation_id='post_vehicle_data_point',
)
async def post_vehicle_data_point(
    entry: EvDataEntry,
    repo: Repository = Depends(get_repository),
):
    """
    Saves a data point for a vehicle in the database
    """
    repo.save_vehicle_data_point(entry=entry)


@app.get('/health', operation_id='health')
async def health(repo: Repository = Depends(get_repository)) -> str:
    """
    Performs a quick health check
    """
    repo.list_vehicle_data_points(
        vehicle_id=None,
        page_size=0,
    )
    return 'OK'
