from sqlalchemy import Column, Integer, String, Numeric, Enum
from app.db.init_db import Base
import enum

class CategoryEnum(str, enum.Enum):
    burgers_rolls = "Бургеры и ролы"
    sauces = "Соусы"
    desserts = "Десерты"
    chicken = "Курочка"
    fries = "Картошка"
    drinks = "Напитки"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)
    image = Column(String, nullable=True)
