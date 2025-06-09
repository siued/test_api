from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.config import settings
from app.routers import health, time
import sentry_sdk as sentry


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Application startup and shutdown events.
    """
    sentry.init(settings.sentry_dsn)  # type: ignore
    yield


app = FastAPI(lifespan=lifespan)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(time.router, prefix="/time", tags=["time"])


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    sentry.capture_exception(exc)
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
