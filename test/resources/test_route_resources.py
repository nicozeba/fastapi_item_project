import pytest

@pytest.fixture
def setup_item_data():
    return {
        "item_1": {"id": 1, "name": "Test Item - 1", "price": 100},
        "item_2": {"id": 2, "name": "Test Item - 2", "price": 200},
        "_last_item_id": 2
    }

@pytest.fixture
def create_item_data():
    return {
        "success_create": {"name": "New Item", "price": 300},
        "missing_name": {"price": 300},
        "missing_price": {"name": "New Item"},
        "missing_name_and_price": {}
    }
    
@pytest.fixture
def update_item_data():
    return {
        "success_update": {"name": "Updated Item", "price": 400},
        "missing_name": {"price": 500},
        "missing_price": {"name": "Updated Item - Newer"},
        "missing_name_and_price": {}
    }