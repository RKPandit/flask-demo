from app import app
import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data
