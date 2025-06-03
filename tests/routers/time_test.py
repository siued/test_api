import pytest

from app.routers.time import is_valid_timezone


@pytest.mark.parametrize(
    "timezone,expected",
    [
        ("UTC", True),
        ("Europe/London", True),
        ("America/New_York", True),
        ("Invalid/Timezone", False),
        ("", False),
        (None, False),
        (123, False),
    ],
)
def test_validate_timezone(timezone: str, expected: bool):
    assert is_valid_timezone(timezone) == expected
