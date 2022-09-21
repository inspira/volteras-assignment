from starlette.config import Config

config = Config(".env")

ALLOWED_ORIGIN = config("ALLOWED_ORIGIN", default="http://localhost:3000")
SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL")

API_DEFAULT_LISTING_LIMIT = 100
