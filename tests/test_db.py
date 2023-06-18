import pytest
import Database.dao_book_manager as dao_book_manager

@pytest.fixture
def setup_connection():
    try:
        connection = dao_book_manager.BookDBManager()
    except:
        connection = None
    finally:
        return connection


def test_connection(setup_connection):
    assert setup_connection != None

def test_getBooks(setup_connection):
    assert setup_connection.getBooks() != None

def test_listBooks(setup_connection):
    with pytest.raises(Exception, match=r"empty"):
        assert setup_connection.searchBooks("", "")
    assert setup_connection.searchBooks("isbn", "isbn") != None

def test_addBook_deleteBook(setup_connection):
    id = setup_connection.addBook("isbn", "name", "writer", "topic", "date", "pagecount", "booknumber", "publisher")
    assert id != None
    assert setup_connection.deleteBook(id) == True


