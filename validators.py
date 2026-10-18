"""Data validation utilities for structure and type checking."""

from typing import Any, Dict, List, Optional, Tuple


def validate_schema(data: Any, schema: Dict[str, Any], allow_extra: bool = True) -> Tuple[bool, List[str]]:
    """
    Validates a dictionary against a specified structural schema.

    Schema keys ending with '?' are treated as optional fields.

    Returns:
        Tuple of (is_valid: bool, list_of_errors: List[str])
    """
    errors = []

    if not isinstance(data, dict):
        return False, [f"Expected dictionary input, got {type(data).__name__}"]

    expected_keys = set()

    for key_spec, expected_type in schema.items():
        is_optional = key_spec.endswith("?")
        key_name = key_spec[:-1] if is_optional else key_spec
        expected_keys.add(key_name)

        if key_name not in data:
            if not is_optional:
                errors.append(f"Missing required key: '{key_name}'")
            continue

        value = data[key_name]
        if value is not None and not isinstance(value, expected_type):
            type_name = getattr(expected_type, '__name__', str(expected_type))
            errors.append(
                f"Key '{key_name}' expected type {type_name}, got {type(value).__name__}"
            )

    if not allow_extra:
        extra_keys = set(data.keys()) - expected_keys
        for extra in extra_keys:
            errors.append(f"Unexpected field present: '{extra}'")

    return len(errors) == 0, errors


def sanitize_string(value: Any, max_len: Optional[int] = None, strip_whitespace: bool = True) -> str:
    """Sanitizes input value to string by stripping whitespace and enforcing max length."""
    if value is None:
        return ""

    result = str(value)

    if strip_whitespace:
        result = result.strip()

    if max_len is not None and max_len > 0:
        result = result[:max_len]

    return result
