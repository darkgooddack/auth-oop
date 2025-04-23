from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.init_db import get_async_session
from app.services.product_service import ProductService
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductInDB

router = APIRouter(prefix="/products", tags=["Products"])

def get_service(session: AsyncSession = Depends(get_async_session)) -> ProductService:
    return ProductService(ProductRepository(session))

@router.get("/", response_model=list[ProductInDB])
async def list_products(service: ProductService = Depends(get_service)):
    return await service.list_products()

@router.get("/{product_id}", response_model=ProductInDB)
async def get_product(product_id: int, service: ProductService = Depends(get_service)):
    product = await service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@router.post("/", response_model=ProductInDB, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, service: ProductService = Depends(get_service)):
    return await service.create_product(product)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, service: ProductService = Depends(get_service)):
    await service.delete_product(product_id)
