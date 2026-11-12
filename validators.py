from typing import Any, Dict, List, Optional

def validate_schema(data: Dict[str, Any], required_keys: List[str]) -> bool:
    """Checks if dictionary contains all required keys."""
    if not isinstance(data, dict):
        return False
    return all(key in data for key in required_keys)

def sanitize_input(data: Any, default: Any = None) -> Any:
    """Returns cleaned value or default if falsy."""
    if data is None or data == '':
        return default
    if isinstance(data, str):
        return data.strip()
    return data

def validate_email(email: str) -> bool:
    """Basic structure verification for email addresses."""
    if not isinstance(email, str) or '@' not in email:
        return False
    parts = email.split('@')
    return len(parts) == 2 and '.' in parts[1]

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Divides list into smaller segments for processing."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [data[i:i + size] for i in range(0, len(data), size)]