"""
API configuration using Starlette
"""
from starlette.config import Config

config = Config(".env")

ALLOWED_ORIGINS = config("ALLOWED_ORIGINS", default=["http://localhost:3000"])
SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL")

API_DEFAULT_LISTING_LIMIT = 100
