import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_credential():
    response = client.post("/credentials/", json={"name": "test", "value": "secret", "type": "API_KEY"})
    assert response.status_code == 200
    assert response.json()["name"] == "test"

def test_read_credential():
    response = client.get("/credentials/test")
    assert response.status_code == 200
    assert response.json()["name"] == "test"