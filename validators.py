import re
from typing import Any, Optional

class InputValidator:
    """Utility for data integrity checks in dev-toolkit-39."""

    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    @staticmethod
    def validate_email(email: str) -> bool:
        """Verify email address format against regex."""
        return bool(InputValidator.EMAIL_PATTERN.match(email))

    @staticmethod
    def validate_range(value: int, min_val: int, max_val: int) -> bool:
        """Ensure integer is within specified bounds."""
        return min_val <= value <= max_val

    @classmethod
    def sanitize_input(cls, data: Any) -> Optional[str]:
        """Strip whitespace and return as string or None."""
        if data is None:
            return None
        return str(data).strip()

def check_required_fields(data: dict, fields: list) -> bool:
    """Validate presence of required keys in dictionary."""
    return all(field in data for field in fields)
