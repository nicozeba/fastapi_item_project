import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_item():
    item_data = {"name": "New Item", "price": 300}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "New Item"
    assert data["price"] == 300
    
def test_create_validate_missing_name_param():
    item_data = {"price": 300}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing name attribute."

def test_create_validate_missing_name_param():
    item_data = {"name": "New Item"}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing price attribute."

def test_create_validate_missing_name_and_price_param():
    item_data = { }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing name attribute."
    assert data["detail"][1] == "Validation Error: missing price attribute."

def test_update_item():
    item_data = {"name": "Updated Item", "price": 400}
    response = client.put("/items/1", json=item_data)
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Updated Item"
    assert data["price"] == 400
    
def test_update_validate_missing_name_param():
    item_data = {"price": 300}
    response = client.put("/items/1", json=item_data)
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing name attribute."

def test_update_validate_missing_name_param():
    item_data = {"name": "New Item"}
    response = client.put("/items/1", json=item_data)
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing price attribute."

def test_update_validate_missing_name_and_price_param():
    item_data = { }
    response = client.put("/items/1", json=item_data)
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing name attribute."
    assert data["detail"][1] == "Validation Error: missing price attribute."

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 204

def test_get_item_not_found():
    response = client.get("/items/9999")
    assert response.status_code == 404
    
def test_update_item_not_found():
    item_data = {"name": "New Item", "price": 300}
    response = client.put("/items/9999", json=item_data)
    assert response.status_code == 404

def test_delete_item_not_found():
    response = client.delete("/items/9999")
    assert response.status_code == 404
