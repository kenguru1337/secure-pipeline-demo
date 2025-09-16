import pytest
from app.app import app  # <-- импортируем экземпляр Flask

# Фикстура для тест-клиента
@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

# Тест главной страницы
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from Secure CI/CD Pipeline!"}

# Тест health endpoint
def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
