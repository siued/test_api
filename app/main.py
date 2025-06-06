from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import health, time


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Application startup and shutdown events.
    """
    # sentry.init(dsn="https://<your_sentry_dsn>", send_default_pii=True)
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(time.router, prefix="/time", tags=["time"])
