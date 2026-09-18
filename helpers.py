import logging
from typing import Any, Callable, Optional, TypeVar

T = TypeVar('T')
logger = logging.getLogger(__name__)

def safe_execute(func: Callable[..., T], *args: Any, default: Optional[T] = None, **kwargs: Any) -> Optional[T]:
    """
    Executes a function with error handling for common edge cases.
    Logs errors and returns a default value on failure.
    """
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"Data validation error in {func.__name__}: {e}")
        return default
    except ConnectionError as e:
        logger.error(f"Network connectivity failure in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system failure in {func.__name__}: {e}", exc_info=True)
        return default

def validate_input(data: Any, expected_type: type) -> bool:
    """
    Validates input type and non-nullity to prevent downstream crashes.
    """
    if data is None:
        return False
    return isinstance(data, expected_type)

def format_data(value: Any) -> str:
    """
    Safely stringifies inputs handling potential conversion errors.
    """
    try:
        return str(value) if value is not None else ""
    except Exception:
        return "<unserializable_data>"