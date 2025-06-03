from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/time")
def get_current_time():
    current_time = datetime.now()
    return {
        "current_time_ISO": current_time.isoformat(),
        "current_time_epoch": int(current_time.timestamp()),
        "current_time_separated": {
            "year": current_time.year,
            "month": current_time.month,
            "day": current_time.day,
            "hour": current_time.hour,
            "minute": current_time.minute,
            "second": current_time.second,
        },
    }
