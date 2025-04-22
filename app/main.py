from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.v1 import user
from app.core.config import api_prefix

app = FastAPI()

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.get("/health")
def healthcheck():
    return {"status": "healthy"}

app.include_router(user.router, prefix=api_prefix + "/users")
