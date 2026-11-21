import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Verify email address format using regex."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Check if value is within inclusive bounds."""
    return min_val <= value <= max_val

def sanitize_string(data: Any) -> str:
    """Ensure input is a clean, stripped string."""
    if not isinstance(data, str):
        return str(data)
    return data.strip()

def is_not_empty(value: Optional[str]) -> bool:
    """Check if string is not null or whitespace."""
    return bool(value and value.strip())