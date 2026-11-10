import re
from typing import Any, Optional

def is_valid_email(email: str) -> bool:
    """Validates email string format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_not_empty(value: Any) -> bool:
    """Checks if value is not None and not empty."""
    if value is None:
        return False
    if isinstance(value, (str, list, dict, set)):
        return len(value) > 0
    return True

def validate_range(value: float, min_val: float, max_val: float) -> bool:
    """Verifies number falls within inclusive bounds."""
    return min_val <= value <= max_val

def sanitize_input(value: str) -> str:
    """Strips whitespace and removes special characters."""
    if not isinstance(value, str):
        return ""
    return re.sub(r'[^a-zA-Z0-9\s]', '', value).strip()

def get_validated_int(value: Any, default: int = 0) -> int:
    """Coerces input to integer or returns default."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default