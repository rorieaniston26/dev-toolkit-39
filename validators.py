import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input_range(value: Any, min_val: int, max_val: int) -> bool:
    """Validates that a numeric input falls within an inclusive range."""
    try:
        if not isinstance(value, (int, float)):
            raise ValidationError(f"Expected numeric type, got {type(value).__name__}")
        
        if not (min_val <= value <= max_val):
            raise ValidationError(f"Value {value} out of bounds [{min_val}, {max_val}]")
            
        return True
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        raise
    except Exception as e:
        logger.critical(f"Unexpected error during validation: {e}")
        return False

def sanitize_string(value: Optional[str], default: str = "") -> str:
    """Safely strips string input or returns default for None."""
    if value is None:
        return default
    if not isinstance(value, str):
        logger.warning(f"Expected string, received {type(value).__name__}")
        return str(value).strip()
    return value.strip()

def check_required_keys(data: dict, keys: list) -> bool:
    """Ensures all required keys exist in dictionary with non-null values."""
    missing = [key for key in keys if key not in data or data[key] is None]
    if missing:
        logger.error(f"Missing required keys: {', '.join(missing)}")
        return False
    return True