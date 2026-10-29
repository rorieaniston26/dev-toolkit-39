class ToolkitError(Exception):
    """Base exception for dev-toolkit-39 operations."""
    pass

class ConfigurationError(ToolkitError):
    """Raised when config files are invalid or missing."""
    pass

class ValidationError(ToolkitError):
    """Raised when input data fails schema validation."""
    pass

class ProcessingError(ToolkitError):
    """Raised when a data transformation fails."""
    pass

def raise_if_none(value: any, name: str) -> None:
    """Utility to enforce non-null arguments."""
    if value is None:
        raise ValidationError(f"Argument '{name}' cannot be None")

def handle_toolkit_error(error: Exception) -> dict:
    """Standardized error reporting structure for the toolkit."""
    if isinstance(error, ToolkitError):
        return {"status": "error", "type": type(error).__name__, "msg": str(error)}
    return {"status": "error", "type": "UnknownError", "msg": "An internal error occurred"}