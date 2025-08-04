from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
    
class ItemRequest(BaseModel):
    name: str
    price: float