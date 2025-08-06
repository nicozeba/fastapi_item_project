from pydantic_core import ValidationError
import pytest
from src.schemas.item_schemas import Item


def test_item_schema_creation():
    item = Item(id=1, name="Test Item", price=300)
    assert item.id == 1
    assert item.name == "Test Item"
    assert item.price == 300

def test_item_schema_missing_id_field():
    with pytest.raises(ValidationError):
        Item(name="Test Item", price=300)  # Missing id

def test_item_schema_missing_name_field():
    with pytest.raises(ValidationError):
        Item(id=1, price=300)  # Missing name

def test_item_schema_missing_price_field():
    with pytest.raises(ValidationError):
        Item(id=1, name="Test Item")  # Missing price
