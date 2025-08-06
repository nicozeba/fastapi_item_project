import pytest

from fastapi.testclient import TestClient
from src.main import app
from src.schemas.item_schemas import Item
from src.routes import item_routes

from test.resources.test_route_resources import setup_item_data, create_item_data, update_item_data

client = TestClient(app)

# This setUp and Teardown is executed before and after each test function
@pytest.fixture(autouse=True)
def setup_items(setup_item_data):
    # Setup
    # Use item_routes to change the state of these variables
    item_routes.items[1] = Item(**setup_item_data["item_1"])
    item_routes.items[2] = Item(**setup_item_data["item_2"])
    item_routes._last_item_id = setup_item_data["_last_item_id"]
    yield
    # Teardown
    item_routes.items.clear()
    item_routes._last_item_id = 0

def test_read_items(setup_item_data):
    response = client.get("/items/")
    items_list = response.json()
    assert response.status_code == 200
    assert isinstance(items_list, list)
    assert len(items_list) == 2
    assert items_list[0] == setup_item_data["item_1"]
    assert items_list[1] == setup_item_data["item_2"]
    
def test_read_item_1(setup_item_data):
    response = client.get("/items/1")
    item = response.json()
    assert response.status_code == 200
    assert item == setup_item_data["item_1"]

def test_create_item(create_item_data):
    response = client.post("/items/", json=create_item_data["success_create"])
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 3
    assert data["name"] == create_item_data["success_create"]["name"]
    assert data["price"] == create_item_data["success_create"]["price"]
    
def test_create_validate_missing_name_param(create_item_data):
    response = client.post("/items/", json=create_item_data["missing_name"])
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing name attribute."

def test_create_validate_missing_name_param(create_item_data):
    response = client.post("/items/", json=create_item_data["missing_price"])
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing price attribute."

def test_create_validate_missing_name_and_price_param(create_item_data):
    response = client.post("/items/", json=create_item_data["missing_name_and_price"])
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing name attribute."
    assert data["detail"][1] == "Validation Error: missing price attribute."

def test_update_item(update_item_data):
    response = client.put("/items/2", json=update_item_data["success_update"])
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["id"] == 2
    assert data["name"] == update_item_data["success_update"]["name"]
    assert data["price"] == update_item_data["success_update"]["price"]
    
def test_update_validate_missing_name_param(update_item_data):
    response = client.put("/items/1", json=update_item_data["missing_name"])
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing name attribute."

def test_update_validate_missing_price_param(update_item_data):
    response = client.put("/items/1", json=update_item_data["missing_price"])
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing price attribute."

def test_update_validate_missing_name_and_price_param(update_item_data):
    response = client.put("/items/1", json=update_item_data["missing_name_and_price"])
    assert response.status_code == 422 
    data = response.json()
    assert data["detail"][0] == "Validation Error: missing name attribute."
    assert data["detail"][1] == "Validation Error: missing price attribute."

def test_delete_item():
    response = client.delete("/items/2")
    assert response.status_code == 204

def test_get_item_not_found():
    response = client.get("/items/9999")
    assert response.status_code == 404
    
def test_update_item_not_found(update_item_data):
    response = client.put("/items/9999", json=update_item_data["success_update"])
    assert response.status_code == 404

def test_delete_item_not_found():
    response = client.delete("/items/9999")
    assert response.status_code == 404
