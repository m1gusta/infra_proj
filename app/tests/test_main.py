from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from Mini Infrastructure App"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }


def test_info():
    response = client.get("/info")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "mini-infra-template"
    assert data["version"] == "1.0.0"
    assert data["hostname"]