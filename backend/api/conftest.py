"""
This code is executed before the test cases
"""

import pytest
from persistence.models import EvDataPointRecord
from persistence.database import get_db_session

@pytest.fixture(scope="class", name='_init_database')
def database():
    """
    Deletes the test database
    """
    session = get_db_session()
    session.query(EvDataPointRecord).delete()
    session.commit()
    session.close()
    yield
