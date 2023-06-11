import pytest
import db_manager

@pytest.fixture
def setup_connection():
    try:
        connection = db_manager.DBManager()
    except:
        connection = None
    finally:
        return connection

def test_connection(setup_connection):
    assert setup_connection != None
