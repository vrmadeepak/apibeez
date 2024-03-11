from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"message": "APIBeez are buzzing...."}