from fastapi import APIRouter
from datetime import datetime

from app.schemas.time import TimeResponse, TimeSeparatedResponse

router = APIRouter()


@router.get("", response_model=TimeResponse)
def get_current_time() -> TimeResponse:
    """
    Get the current time in various formats.
    Returns:
        CurrentTimeResponse: A response containing the current time in ISO format,
        epoch timestamp, and separated components (year, month, day, hour, minute, second).
    """
    current_time = datetime.now()
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
