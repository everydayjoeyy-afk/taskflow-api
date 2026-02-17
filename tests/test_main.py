import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "Application is running"}

def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Write more tests"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Write more tests"
    assert data["completed"] is False
    assert "id" in data
