# -*- coding: utf-8 -*-
"""
API configuration using Starlette
"""
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config('.env')

ALLOWED_ORIGINS = config(
    'ALLOWED_ORIGINS',
    default=['http://localhost:3000'],
    cast=CommaSeparatedStrings
)
SQLALCHEMY_DATABASE_URL = config('SQLALCHEMY_DATABASE_URL')

API_DEFAULT_LISTING_LIMIT = 100
