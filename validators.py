import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def validate_input(data: Any, expected_type: type) -> Optional[Any]:
    """Ensures input matches expected type with edge case handling."""
    try:
        if data is None:
            raise ValueError("Input data cannot be null")
        
        if not isinstance(data, expected_type):
            raise TypeError(f"Expected {expected_type.__name__}, got {type(data).__name__}")
            
        return data
    except (ValueError, TypeError) as e:
        logger.error(f"Validation failed: {e}")
        return None

def sanitize_string(value: Any) -> str:
    """Cleans string input or returns empty default."""
    try:
        if not isinstance(value, str):
            return ""
        return value.strip()
    except Exception as e:
        logger.warning(f"Unexpected error during sanitization: {e}")
        return ""

def safe_division(numerator: float, denominator: float) -> float:
    """Performs division with zero division protection."""
    try:
        return float(numerator) / float(denominator)
    except ZeroDivisionError:
        logger.error("Attempted division by zero")
        return 0.0
    except (ValueError, TypeError):
        logger.error("Invalid numeric input for division")
        return 0.0