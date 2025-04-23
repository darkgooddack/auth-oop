from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
from app.models.product import CategoryEnum

class ProductBase(BaseModel):
    name: str
    price: Decimal
    category: CategoryEnum
    image: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: int

    class Config:
        from_attributes = True
