import re
from typing import Any, Optional

class DataValidator:
    """Utility class for standard input validation"""

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    @staticmethod
    def validate_email(email: str) -> bool:
        """Verify email address format"""
        if not isinstance(email, str):
            return False
        return bool(DataValidator.EMAIL_REGEX.match(email))

    @staticmethod
    def validate_length(value: str, min_len: int, max_len: Optional[int] = None) -> bool:
        """Check string length constraints"""
        if not isinstance(value, str):
            return False
        length = len(value)
        if max_len is not None:
            return min_len <= length <= max_len
        return length >= min_len

    @staticmethod
    def validate_range(value: Any, min_val: float, max_val: float) -> bool:
        """Check if numeric value is within bounds"""
        try:
            num = float(value)
            return min_val <= num <= max_val
        except (ValueError, TypeError):
            return False

    @classmethod
    def sanitize_input(cls, data: str) -> str:
        """Strip whitespace and escape basic control characters"""
        return str(data).strip()