"""Data validation utility module with robust error handling for edge cases."""

from typing import Any, Dict, List, Optional, Union
import re


class ValidationError(ValueError):
    """Custom exception raised when data validation fails."""
    pass


def validate_email(email: Any) -> str:
    """Validate and sanitize email address string."""
    if email is None:
        raise ValidationError("Email address cannot be None")

    if not isinstance(email, str):
        raise ValidationError(f"Expected string for email, got {type(email).__name__}")

    cleaned = email.strip()
    if not cleaned:
        raise ValidationError("Email address cannot be empty")

    if len(cleaned) > 254:
        raise ValidationError("Email address exceeds maximum length of 254 chars")

    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, cleaned):
        raise ValidationError(f"Invalid email format: '{cleaned}'")

    return cleaned.lower()


def validate_numeric_range(
    val: Any,
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
) -> Union[int, float]:
    """Validate numeric input ensuring it fits within optional bounds."""
    if val is None or isinstance(val, bool):
        raise ValidationError("Numeric value cannot be None or boolean")

    try:
        num = float(val) if "." in str(val) else int(val)
    except (ValueError, TypeError):
        raise ValidationError(f"Cannot parse '{val}' as a numeric value")

    if min_val is not None and num < min_val:
        raise ValidationError(f"Value {num} is below minimum ({min_val})")

    if max_val is not None and num > max_val:
        raise ValidationError(f"Value {num} exceeds maximum ({max_val})")

    return num


def validate_dict_schema(data: Any, required_keys: List[str]) -> Dict[str, Any]:
    """Ensure input is a dictionary containing required non-null keys."""
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dict, got {type(data).__name__}")

    missing = [k for k in required_keys if k not in data or data[k] is None]
    if missing:
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")

    return data