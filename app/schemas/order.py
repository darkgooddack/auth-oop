from pydantic import BaseModel
from typing import List
from decimal import Decimal

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    customer_id: int
    random_number: int
    items: List[OrderItemCreate]

class OrderItemResponse(OrderItemCreate):
    price_item: Decimal

class OrderResponse(BaseModel):
    id: int
    customer_id: int
    random_number: int
    total_price: Decimal
    items: List[OrderItemResponse]

    class Config:
        from_attribute = True