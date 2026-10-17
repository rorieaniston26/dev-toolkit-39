class ToolkitError(Exception):
    """Base exception for dev-toolkit-39."""
    pass

class ValidationError(ToolkitError):
    """Raised when input validation fails."""
    pass

class ConfigurationError(ToolkitError):
    """Raised when environment configuration is missing."""
    pass

class ExecutionError(ToolkitError):
    """Raised when a process fails to complete."""
    def __init__(self, message, exit_code=1):
        super().__init__(message)
        self.exit_code = exit_code

def raise_if_none(value, message="Value cannot be None"):
    """Helper to enforce non-null constraints."""
    if value is None:
        raise ValidationError(message)
    return value

def safe_execute(func, *args, **kwargs):
    """Wraps execution to handle toolkit-specific exceptions."""
    try:
        return func(*args, **kwargs)
    except ToolkitError as e:
        # Log here if a logger is attached
        raise e
    except Exception as e:
        raise ExecutionError(f"Unexpected error: {str(e)}")