"""Custom exception hierarchy and error handling utilities."""

from typing import Any, Dict, Optional


class ToolkitError(Exception):
    """Base exception class for dev-toolkit errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        """Serialize error information for logging or API responses."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
        }


class ValidationError(ToolkitError):
    """Raised when input validation fails for edge cases."""

    pass


class ResourceNotFoundError(ToolkitError):
    """Raised when a required file or resource cannot be located."""

    pass


class ConfigurationError(ToolkitError):
    """Raised when configuration values are missing or malformed."""

    pass


def handle_edge_case(
    value: Any, expected_type: type, fallback: Any = None
) -> Any:
    """Safely cast or parse values, returning fallback on type failure."""
    if value is None:
        return fallback
    try:
        return expected_type(value)
    except (ValueError, TypeError) as err:
        raise ValidationError(
            f"Failed to parse value '{value}' as {expected_type.__name__}",
            details={"original_value": repr(value), "error": str(err)},
        ) from err
