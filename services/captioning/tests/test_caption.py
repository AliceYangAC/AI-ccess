from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_caption_endpoint():
    with open("image2.jpg", "rb") as img:
        response = client.post("/caption", files={"file": img})
    assert response.status_code == 200
    assert "caption" in response.json()
