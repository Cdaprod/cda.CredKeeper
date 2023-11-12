import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
import pytest
from main import app
from models import CredentialDB, CredentialType

client = TestClient(app)

@pytest.fixture(scope="function")
def populate_fake_data(db_session):
    test_credential = CredentialDB(name="test1", value="value1", type=CredentialType.API_KEY)
    db_session.add(test_credential)
    db_session.commit()  # Commit the session to save the data
    yield
    db_session.delete(test_credential)
    db_session.commit()  # Clean up after the test

def test_read_credential_with_fake_data(populate_fake_data, db_session):
    response = client.get("/credentials/test1")
    assert response.status_code == 200