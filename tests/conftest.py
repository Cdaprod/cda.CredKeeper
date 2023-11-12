import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from __init__ import Base

@pytest.fixture(scope="function")
def db_session():
    # Create an in-memory SQLite database for testing
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(engine)
