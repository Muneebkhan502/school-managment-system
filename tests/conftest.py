from fastapi.testclient import TestClient
from main import app
from database import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
TEST_DATABASE_URL = "sqlite:///./test_student.db"  # This is the URL for the test SQLite database, it specifies that we want to use SQLite and the database file is test_student.db
@pytest.fixture()
def client():
    engine = create_engine(TEST_DATABASE_URL,connect_args={"check_same_thread": False})  # This line creates a SQLAlchemy engine that will manage the connection to the test database. The connect_args parameter is used to specify that we want to use the same thread for the connection, which is required for SQLite.
    TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)
    def override_get_db():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    Base.metadata.drop_all(engine)

@pytest.fixture()
def registered_user(client):
    response = client.post("/users/", json = {
        "username": "testuser",
        "email": "testuser@example.com",
        "role": "admin",
        "password": "testpassword"})
    print(f"Registered User Response: {response.json()}")
    print(response.status_code)
    return {"username":"testuser","email":"testuser@example.com","role":"admin","password":"testpassword"}
    