from pydantic_core import ValidationError
import pytest
from src.schemas.item_schemas import Item

@pytest.mark.parametrize("expect_item_id, expect_item_name, expect_item_price", [
    (1, "Test Item", 300)
])
def test_item_schema_creation(expect_item_id, expect_item_name, expect_item_price):
    item = Item(id=expect_item_id, name=expect_item_name, price=expect_item_price)
    assert item.id == expect_item_id
    assert item.name == expect_item_name
    assert item.price == expect_item_price

@pytest.mark.parametrize("item_name, item_price", [
    ("Test Item", 300)
])
def test_item_schema_missing_id_field(item_name, item_price):
    with pytest.raises(ValidationError):
        Item(name=item_name, price=item_price)  # Missing id

@pytest.mark.parametrize("item_id, item_price", [
    (1, 300)
])
def test_item_schema_missing_name_field(item_id, item_price):
    with pytest.raises(ValidationError):
        Item(id=item_id, price=item_price)  # Missing name

@pytest.mark.parametrize("item_id, item_name", [
    (1, "Test Item")
])
def test_item_schema_missing_price_field(item_id, item_name):
    with pytest.raises(ValidationError):
        Item(id=item_id, name=item_name)  # Missing price
