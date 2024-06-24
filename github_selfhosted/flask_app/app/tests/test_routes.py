import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_index(client):
    rv = client.get('/')
    assert rv.data == b"Hello, World!"
