
from typing import Dict, List
from fastapi import APIRouter, HTTPException, status

from item_be.src.constants import MESSAGE_ERROR_MISSING_ITEM
from item_be.src.schemas.item_schemas import Item, ItemRequest


router = APIRouter()

items: Dict[int, Item] = {}
_last_item_id = 0

@router.get("/item", response_model=List[Item])
def read_all_items():
  return list(items.values())

@router.get("/item/{item_id}", response_model=Item)
def read_item_by_id(item_id : int):
  if item_id not in items.keys():
      raise HTTPException(status_code=404, detail=[MESSAGE_ERROR_MISSING_ITEM])
  return items[item_id]

@router.post("/item", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item : ItemRequest):
  global _last_item_id
  _last_item_id += 1
  new_item = Item(id=_last_item_id, **item.model_dump())
  items[_last_item_id] = new_item
  return new_item

@router.put("/item/{item_id}", response_model=Item)
def update_item(item_id : int, new_item : ItemRequest):
  if item_id not in items.keys():
      raise HTTPException(status_code=404, detail=[MESSAGE_ERROR_MISSING_ITEM])
  items[item_id].name = new_item.name
  items[item_id].price = new_item.price
  return items[item_id]

@router.delete("/item/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id : int):
  if item_id not in items.keys():
      raise HTTPException(status_code=404, detail=[MESSAGE_ERROR_MISSING_ITEM])
  item = items.pop(item_id)
  return item