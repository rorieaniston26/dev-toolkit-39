import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def validate_input(data: Any, expected_type: type) -> Optional[Any]:
    """Validate input data against expected type with robust error handling."""
    try:
        if data is None:
            raise ValueError("Input data cannot be None")
        
        if not isinstance(data, expected_type):
            raise TypeError(f"Expected {expected_type.__name__}, got {type(data).__name__}")
            
        return data
    except (ValueError, TypeError) as e:
        logger.error(f"Validation failed: {e}")
        return None
    except Exception as e:
        logger.critical(f"Unexpected error during validation: {e}")
        raise

def safe_access(container: dict, key: str, default: Any = None) -> Any:
    """Access dictionary keys safely without raising KeyError."""
    try:
        if not isinstance(container, dict):
            raise ValueError("Container must be a dictionary")
        return container.get(key, default)
    except Exception as e:
        logger.warning(f"Access error for key '{key}': {e}")
        return default

def sanitize_numeric(value: Any) -> float:
    """Convert input to float with defensive conversion logic."""
    try:
        return float(value)
    except (ValueError, TypeError, OverflowError):
        logger.debug(f"Conversion failed for value: {value}, defaulting to 0.0")
        return 0.0