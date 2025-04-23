from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.jwt import get_current_user
from app.db.init_db import get_async_session
from app.models.user import User
from app.services.order_service import OrderService
from app.repositories.order_repository import OrderRepository
from app.schemas.order import OrderCreate, OrderResponse

router = APIRouter(prefix='/orders', tags=['Orders'])

def get_order_service(session: AsyncSession = Depends(get_async_session)) -> OrderService:
    order_repository = OrderRepository(session)
    return OrderService(order_repository)

@router.post("/", response_model=OrderResponse)
async def create_order(
    order_data: OrderCreate,
    order_service: OrderService = Depends(get_order_service),
):
    try:
        return await order_service.create_order(order_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating order: " + str(e))


@router.get("/my", response_model=List[OrderResponse])
async def get_my_orders(
    order_service: OrderService = Depends(get_order_service),
    current_user: User = Depends(get_current_user),
):
    return await order_service.get_user_orders(current_user.id)