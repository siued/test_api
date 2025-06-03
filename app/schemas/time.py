from pydantic import BaseModel


class TimeSeparatedResponse(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int


class TimeResponse(BaseModel):
    current_time_ISO: str
    current_time_epoch: int
    current_time_separated: TimeSeparatedResponse
