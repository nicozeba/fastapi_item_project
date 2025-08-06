import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_main_root():
    response = client.get("/")
    assert response.status_code == 404
