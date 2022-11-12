import pytest
#from app.connection import DBConnection

@pytest.fixture(scope= "module")
def get_database():
    """ Fixture to get the connection test data """
    #db = DBConnection()
    return None