from fastapi import APIRouter

from app.schemas.health import HealthResponse

router = APIRouter()


@router.get("/", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """
    Health check endpoint to verify the service is running.
    Returns:
        HealthResponse: A response indicating the service status.
    """
    return HealthResponse(status="ok")
