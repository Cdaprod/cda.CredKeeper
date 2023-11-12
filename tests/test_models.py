import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, CredentialDB, CredentialType

TEST_DATABASE_URL = "sqlite:///./test.db"  # SQLite will create this file if it doesn't exist
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_credential(db_session):
    new_credential = CredentialDB(name="test_credential", value="test_value", type=CredentialType.API_KEY)
    db_session.add(new_credential)
    db_session.commit()
    assert db_session.query(CredentialDB).filter_by(name="test_credential").first() is not None
