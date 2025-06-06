import random
from zoneinfo import ZoneInfo
from app.services.exceptions_service import ExceptionsService
from fastapi import APIRouter, Depends, Query, HTTPException
from datetime import datetime

from app.schemas.time import TimeResponse, TimeSeparatedResponse

router = APIRouter()


def is_valid_timezone(timezone: str) -> bool:
    try:
        ZoneInfo(timezone)
        return True
    except Exception:
        return False


@router.get(
    "",
    response_model=TimeResponse,
    responses={
        400: {
            "description": "Invalid timezone",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid timezone: Europe/Invalid"}
                }
            },
        },
    },
)
async def get_current_time(
    timezone: str = Query(
        "UTC",
        description="Timezone in IANA format (e.g., 'UTC', 'Europe/London', 'America/New_York').",
        examples=["UTC", "Europe/London", "America/New_York"],
    ),
    service: ExceptionsService = Depends(ExceptionsService),
) -> TimeResponse:
    """
    Get the current time in various formats.
    """

    if random.random() < 0.5:
        service.throw_random_exception()

    if not is_valid_timezone(timezone):
        raise HTTPException(status_code=400, detail=f"Invalid timezone: {timezone}")
    current_time = datetime.now(ZoneInfo(timezone))
    return TimeResponse(
        current_time_ISO=current_time.isoformat(),
        current_time_epoch=int(current_time.timestamp()),
        current_time_separated=TimeSeparatedResponse(
            year=current_time.year,
            month=current_time.month,
            day=current_time.day,
            hour=current_time.hour,
            minute=current_time.minute,
            second=current_time.second,
        ),
    )
