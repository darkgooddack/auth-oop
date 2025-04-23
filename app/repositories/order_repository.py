from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from app.models.order import Order, OrderStatus
from app.models.order_item import OrderItem
from app.models.product import Product
from app.schemas.order import OrderCreate
from decimal import Decimal
from sqlalchemy import func

class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_order(self, order_data: OrderCreate) -> Order:
        total = Decimal("0.00")
        items = []

        for item in order_data.items:
            result = await self.session.execute(select(Product).filter(Product.id == item.product_id))
            product = result.scalars().first()

            if product is None:
                raise ValueError(f"Product with id {item.product_id} not found")

            price = product.price * item.quantity
            total += price
            items.append(OrderItem(
                product_id=item.product_id,
                quantity=item.quantity,
                price_item=price
            ))

        order = Order(
            random_number=order_data.random_number,
            customer_id=order_data.customer_id,
            status=OrderStatus.none,
            total_price=total,
            items=items,
            created_at=func.now()
        )

        self.session.add(order)
        await self.session.commit()

        result = await self.session.execute(
            select(Order).options(selectinload(Order.items)).filter(Order.id == order.id)
        )
        order = result.scalar_one()

        return order

    async def get_orders_by_user(self, user_id: int) -> List[Order]:
        result = await self.session.execute(
            select(Order)
            .options(selectinload(Order.items))
            .filter(Order.customer_id == user_id)
            .order_by(Order.created_at.desc())
        )
        return result.scalars().all()