"""
Abstract factory for the sqlalchemy repo
"""

from .sqlalchemy_repository import SqlAlchemyRepository
from .database import get_db_session

def get_repository():
    """
    Creates a new session and injects it into the repository
    """
    try:
        db_session = get_db_session()
        repo = SqlAlchemyRepository(db_session)
        yield repo
    finally:
        db_session.close()
