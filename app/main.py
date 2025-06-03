from fastapi import FastAPI
from app.routers import health, time

app = FastAPI()


app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(time.router, prefix="/time", tags=["time"])
