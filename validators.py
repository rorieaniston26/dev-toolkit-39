import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Verify email address format using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def ensure_list(data: Any) -> list:
    """Convert single items or None to a list."""
    if data is None:
        return []
    if isinstance(data, list):
        return data
    return [data]

def clean_string(value: Optional[str], default: str = "") -> str:
    """Strip whitespace and provide default for nulls."""
    if not value:
        return default
    return str(value).strip()

def is_numeric(value: Any) -> bool:
    """Check if input represents a number."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False