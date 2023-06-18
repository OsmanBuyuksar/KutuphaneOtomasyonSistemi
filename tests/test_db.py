import pytest
import Database.dao_book_manager as dao_book_manager

@pytest.fixture
def setup_connection():
    try:
        connection = dao_book_manager.DBManager()
    except:
        connection = None
    finally:
        return connection

def test_connection(setup_connection):
    assert setup_connection != None

