import pytest
from starlette.testclient import TestClient


@pytest.fixture
def test_client():
    from app.main import app

    yield TestClient(app)


def test_app(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_html2text(test_client):
    response = test_client.post("/html2text", json={"html": "<h1>Hello, World!</h1>"})
    assert response.status_code == 200
    assert response.json() == {"text": "Hello, World!"}
