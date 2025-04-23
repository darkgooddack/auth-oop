from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.product import Product
from app.repositories.base import AbstractRepository

class ProductRepository(AbstractRepository[Product]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id: int):
        result = await self.session.execute(select(Product).where(Product.id == id))
        return result.scalars().first()

    async def list(self):
        result = await self.session.execute(select(Product))
        return result.scalars().all()

    async def add(self, obj: Product):
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def delete(self, id: int):
        obj = await self.get(id)
        if obj:
            await self.session.delete(obj)
            await self.session.commit()
