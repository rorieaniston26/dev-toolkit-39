import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """
    Executes a callable safely with broad exception handling.
    Returns None if an error occurs to maintain flow.
    """
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"Data validation error in {func.__name__}: {e}")
    except Exception as e:
        logger.critical(f"Unexpected system error in {func.__name__}: {e}")
    return None

def parse_int_safe(value: Any, default: int = 0) -> int:
    """
    Converts value to integer with graceful fallback.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        logger.warning(f"Failed to cast {value} to int, returning default {default}")
        return default

def validate_payload(data: Optional[dict], required_keys: list[str]) -> bool:
    """
    Checks for existence of keys in a dictionary safely.
    """
    if not isinstance(data, dict):
        return False
    
    return all(key in data for key in required_keys)