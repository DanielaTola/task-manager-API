import pytest
from fastapi.testclient import TestClient

from app.core.database import get_db
from app.main import app
from test.database_test import TestingSessionLocal, create_test_db

create_test_db()


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session")
def client():
    yield TestClient(app)
