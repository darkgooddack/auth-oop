import redis.asyncio as redis

from app.core.config import settings

r = redis.from_url(f"redis://{settings.redis_host}:{settings.redis_port}/{settings.redis_db}")

async def store_refresh_token(user_id: int, refresh_token: str):
    await r.set(f"user:{user_id}:refresh_token", refresh_token, ex=60 * 60 * 24 * 7)

async def get_refresh_token(user_id: int):
    return await r.get(f"user:{user_id}:refresh_token")

async def revoke_refresh_token(user_id: int):
    await r.delete(f"user:{user_id}:refresh_token")
