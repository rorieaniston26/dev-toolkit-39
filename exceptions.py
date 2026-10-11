"""Custom exception hierarchy and error context wrappers for dev-toolkit-39."""

from typing import Any, Dict, Optional


class ToolkitError(Exception):
    """Base exception class for all toolkit operational errors."""

    def __init__(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.context = context or {}

    def to_dict(self) -> Dict[str, Any]:
        """Serialize exception details for structured logging or API responses."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "context": self.context,
        }


class ValidationError(ToolkitError):
    """Raised when input validation fails or data criteria are not met."""

    def __init__(self, message: str, field: Optional[str] = None, value: Any = None) -> None:
        context = {"field": field, "invalid_value": repr(value)} if field else {}
        super().__init__(message, context=context)


class ConfigurationError(ToolkitError):
    """Raised when configuration settings are missing or invalid."""
    pass


class ResourceNotFoundError(ToolkitError):
    """Raised when a required file or resource cannot be located."""

    def __init__(self, resource_type: str, resource_id: str) -> None:
        message = f"Resource '{resource_id}' of type '{resource_type}' was not found."
        super().__init__(message, context={"type": resource_type, "id": resource_id})


class ProcessingError(ToolkitError):
    """Raised when an unexpected error occurs during data processing."""

    def __init__(self, message: str, original_error: Optional[BaseException] = None) -> None:
        context = {}
        if original_error:
            context["cause"] = str(original_error)
            context["cause_type"] = original_error.__class__.__name__
        super().__init__(message, context=context)
        if original_error:
            self.__cause__ = original_error
