import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input_data(data: Any, expected_type: type) -> bool:
    """Validates data types and handles potential edge cases like None."""
    if data is None:
        logger.error("Validation failed: input data is None")
        raise ValidationError("Input data cannot be null")

    if not isinstance(data, expected_type):
        logger.warning(f"Type mismatch: expected {expected_type}, got {type(data)}")
        return False

    return True

def safe_dict_get(data: dict, key: str, default: Any = None) -> Any:
    """Safely retrieves values from dictionaries with fallback handling."""
    try:
        if not isinstance(data, dict):
            raise ValueError("Provided data is not a dictionary")
        return data.get(key, default)
    except (AttributeError, ValueError) as e:
        logger.error(f"Dictionary access error: {e}")
        return default

def validate_numeric_range(value: Any, min_val: float, max_val: float) -> bool:
    """Checks if a value falls within a specific range."""
    try:
        num = float(value)
        return min_val <= num <= max_val
    except (TypeError, ValueError):
        logger.debug(f"Invalid numeric input received: {value}")
        return False