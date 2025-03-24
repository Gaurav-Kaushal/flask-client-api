import pytest
from app import create_app
from app.db import get_db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()
    return client

def test_get_clients(client):
    response = client.get("/clients")
    assert response.status_code == 200

def test_add_client(client):
    response = client.post("/clients", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
