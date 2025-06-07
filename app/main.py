from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI
from app.config import settings
from app.routers import health, time


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Application startup and shutdown events.
    """
    yield


app = FastAPI(lifespan=lifespan)

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
# )

logging.info(settings.postgres_user)


app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(time.router, prefix="/time", tags=["time"])
