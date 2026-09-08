import json
from typing import Any, Dict, Optional, Type, TypeVar

T = TypeVar("T")


def safe_get_nested(
    data: Any, path: str, default: Any = None, expected_type: Optional[Type[T]] = None
) -> Any:
    """Safely retrieves a nested value from a dictionary or list using dot notation.

    Handles edge cases like None values, invalid paths, and mismatched
    types.
    """
    if not data:
        return default

    parts = path.split(".")
    current = data

    try:
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
            elif isinstance(current, list):
                try:
                    idx = int(part)
                    current = current[idx]
                except (ValueError, IndexError):
                    return default
            else:
                return default

            if current is None:
                return default

        if expected_type is not None:
            if not isinstance(current, expected_type):
                try:
                    return expected_type(current)
                except (ValueError, TypeError):
                    return default

        return current
    except Exception:
        return default


def parse_json_safely(raw_data: Any, fallback: Optional[Dict] = None) -> Dict:
    """Parses JSON strings or returns dictionary representation safely.

    Handles dirty edge cases like non-string inputs, malformed JSON, and
    None.
    """
    if fallback is None:
        fallback = {}

    if raw_data is None:
        return fallback

    if isinstance(raw_data, dict):
        return raw_data

    if not isinstance(raw_data, (str, bytes)):
        return fallback

    try:
        parsed = json.loads(raw_data)
        return parsed if isinstance(parsed, dict) else fallback
    except (json.JSONDecodeError, TypeError):
        return fallback
