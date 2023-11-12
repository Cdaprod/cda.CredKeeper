import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
import pytest
from main import app
from models import CredentialDB, CredentialType

client = TestClient(app)

@pytest.fixture(scope="function")
def create_test_credential(db_session):
    credential = CredentialDB(name="test", value="test_value", type=CredentialType.API_KEY)
    db_session.add(credential)
    db_session.commit()
    yield
    db_session.delete(credential)
    db_session.commit()

def test_read_credential(db_session, create_test_credential):
    response = client.get("/credentials/test")
    assert response.status_code == 200
