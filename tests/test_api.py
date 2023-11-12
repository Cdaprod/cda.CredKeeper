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
    fake_credentials = [
        CredentialDB(name="test1", value="value1", type=CredentialType.API_KEY),
        CredentialDB(name="test2", value="value2", type=CredentialType.SSH_KEY),
        # Add as many fake credentials as needed
    ]

    for credential in fake_credentials:
        db_session.add(credential)
    db_session.commit()

    yield

    for credential in fake_credentials:
        db_session.delete(credential)
    db_session.commit()

def test_read_credential_with_fake_data(populate_fake_data, db_session):
    response = client.get("/credentials/test1")
    assert response.status_code == 200

@pytest.fixture(scope="function")
def create_test_credential(db_session):
    credential = CredentialDB(name="test", value="test_value", type=CredentialType.API_KEY)
    db_session.add(credential)
    db_session.commit()
    yield
    db_session.delete(credential)
    db_session.commit()

def test_read_credential_with_single_entry(create_test_credential, db_session):
    response = client.get("/credentials/test")
    assert response.status_code == 200