import typing
import datetime
import logging

logger = logging.getLogger(__name__)

def format_timestamp(dt: datetime.datetime, fmt: str = '%Y-%m-%d %H:%M:%S') -> str:
    """Converts a datetime object to a formatted string."""
    try:
        return dt.strftime(fmt)
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid datetime format input: {e}")
        return ""

def get_chunked_list(items: typing.List[typing.Any], size: int) -> typing.Generator[typing.List[typing.Any], None, None]:
    """Yields successive n-sized chunks from a list."""
    if size <= 0:
        yield items
        return
    for i in range(0, len(items), size):
        yield items[i : i + size]

def sanitize_string(text: typing.Optional[str]) -> str:
    """Removes whitespace and ensures string output."""
    if not text:
        return ""
    return str(text).strip()

def calculate_duration_seconds(start: datetime.datetime, end: datetime.datetime) -> float:
    """Returns the difference between two timestamps in seconds."""
    delta = end - start
    return float(delta.total_seconds())