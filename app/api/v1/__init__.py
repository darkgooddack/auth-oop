from .users import router as users_router
from .products import router as products_router
from .order import router as orders_router

routers = [
    users_router,
    products_router,
    orders_router,
]
