from random import choices, uniform
from string import ascii_letters

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.backend.database import Base
from src.backend.main import app, get_db

DATABASE_URL = "sqlite://"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def random_string(n=32):
    return "".join(choices(ascii_letters, k=n))


def random_double():
    return round(uniform(0.0, 100.0), 2)


product = {
    "name": random_string(),
    "description": random_string(512),
    "price": random_double(),
}


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_empty_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_product():
    response = client.post(
        "/products/",
        json=product,
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, **product}


def test_read_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, **product}


def test_read_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, **product}]


def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, **product}
    response = client.get("/products/1")
    assert response.status_code == 404


def test_read_deleted_empty_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []