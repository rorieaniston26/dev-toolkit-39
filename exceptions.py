class ToolkitError(Exception):
    """Base exception for dev-toolkit-39 operations."""
    pass

class ConfigurationError(ToolkitError):
    """Raised when configuration settings are invalid."""
    pass

class ValidationError(ToolkitError):
    """Raised when input validation fails."""
    pass

class OperationTimeoutError(ToolkitError):
    """Raised when a process exceeds allotted time."""
    pass

def raise_if_none(value, message="Value cannot be None"):
    """Utility to enforce non-null values."""
    if value is None:
        raise ValidationError(message)

def handle_toolkit_exception(e):
    """Standardized exception formatting helper."""
    if isinstance(e, ToolkitError):
        return f"[Toolkit Error] {type(e).__name__}: {str(e)}"
    return f"[Unexpected Error] {type(e).__name__}: {str(e)}"

if __name__ == "__main__":
    # Example usage
    try:
        raise_if_none(None, "Initialization failed")
    except ValidationError as e:
        print(handle_toolkit_exception(e))