import re
from typing import Any, Optional

class DataValidator:
    """Utility for data integrity checks."""

    EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    @staticmethod
    def validate_email(email: str) -> bool:
        """Verify email address string format."""
        if not isinstance(email, str):
            return False
        return bool(DataValidator.EMAIL_PATTERN.match(email))

    @staticmethod
    def validate_range(value: Any, min_val: float, max_val: float) -> bool:
        """Check if numerical value is in range."""
        try:
            num = float(value)
            return min_val <= num <= max_val
        except (TypeError, ValueError):
            return False

    @staticmethod
    def sanitize_input(data: Optional[str]) -> str:
        """Strip whitespace and normalize input string."""
        if data is None:
            return ""
        return str(data).strip()

    @classmethod
    def validate_payload(cls, data: dict, required_keys: list) -> bool:
        """Ensure all required keys exist and are non-empty."""
        return all(data.get(k) for k in required_keys)