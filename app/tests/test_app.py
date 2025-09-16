import pytest
from app.app import app  # Импортируем экземпляр Flask

# Фикстура для тест-клиента
@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

# Тест главной страницы
def test_home(client):
    response = client.get('/')
    if response.status_code != 200:
        raise AssertionError(f"Expected 200 OK, got {response.status_code}")
    if response.get_json() != {"message": "Hello from Secure CI/CD Pipeline!"}:
        raise AssertionError(f"Response JSON mismatch: {response.get_json()}")

# Тест health endpoint
def test_health(client):
    response = client.get('/health')
    if response.status_code != 200:
        raise AssertionError(f"Expected 200 OK, got {response.status_code}")
    if response.get_json() != {"status": "ok"}:
        raise AssertionError(f"Response JSON mismatch: {response.get_json()}")

