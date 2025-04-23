from app.models.product import Product
from app.schemas.product import ProductCreate
from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def get_product(self, id: int) -> Product:
        return await self.repository.get(id)

    async def list_products(self):
        return await self.repository.list()

    async def create_product(self, data: ProductCreate):
        product = Product(**data.dict())
        return await self.repository.add(product)

    async def delete_product(self, id: int):
        await self.repository.delete(id)
