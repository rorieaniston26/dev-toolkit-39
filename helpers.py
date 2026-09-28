import logging
from typing import Any, Optional, Callable

logger = logging.getLogger('dev-toolkit-39')

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Execute function with robust error handling for edge cases."""
    try:
        return func(*args, **kwargs)
    except TypeError as e:
        logger.error(f"Invalid arguments provided to {func.__name__}: {e}")
    except ValueError as e:
        logger.error(f"Invalid value encountered in {func.__name__}: {e}")
    except AttributeError as e:
        logger.error(f"Attribute error in {func.__name__}: {e}")
    except Exception as e:
        logger.critical(f"Unexpected failure in {func.__name__}: {type(e).__name__} - {e}")
    return None

def sanitize_input(value: Any, default: Any = None) -> Any:
    """Validate and sanitize user input with fallback."""
    if value is None or (isinstance(value, str) and not value.strip()):
        return default
    return value

def format_response(data: Any) -> dict:
    """Ensure consistent output structure for API responses."""
    if data is None:
        return {"status": "error", "data": None}
    return {"status": "success", "data": data}