import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_credential():
    payload = {
        "name": "test",
        "value": "secret",  # Make sure this is a valid secret string
        "type": "API_KEY",  # Ensure this matches the enum in your schema
        # Include any other required fields defined in your schema
    }
    response = client.post("/credentials/", json=payload)
    assert response.status_code == 200


def test_read_credential():
    response = client.get("/credentials/test")
    assert response.status_code == 200
    assert response.json()["name"] == "test"