from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.order import OrderCreate
from app.repositories.order_repository import OrderRepository
from app.models.order import Order

class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    async def create_order(self, order_data: OrderCreate) -> Order:
        return await self.repository.create_order(order_data)

    async def get_user_orders(self, user_id: int) -> List[Order]:
        return await self.repository.get_orders_by_user(user_id)