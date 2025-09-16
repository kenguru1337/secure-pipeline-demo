import pytest
from app.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    if response.status_code != 200:
        raise AssertionError(f"Expected 200 OK, got {response.status_code}")
    if response.get_json() != {"message": "Hello from Secure CI/CD Pipeline!"}:
        raise AssertionError(f"Response JSON mismatch: {response.get_json()}")

def test_health(client):
    response = client.get('/health')
    if response.status_code != 200:
        raise AssertionError(f"Expected 200 OK, got {response.status_code}")
    if response.get_json() != {"status": "ok"}:
        raise AssertionError(f"Response JSON mismatch: {response.get_json()}")

