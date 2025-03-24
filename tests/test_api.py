import pytest
from app import create_app
from app.db import get_db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.app_context():
        db = get_db()
        if db:
            db.clients.delete_many({}) 

    client = app.test_client()
    return client

def test_get_clients(client):
    response = client.get("/clients")
    assert response.status_code == 200

def test_add_client(client):
    response = client.post("/clients", json={"name": "GK", "email": "GK@example.com"})
    assert response.status_code == 201
