class DevToolkitError(Exception):
    """Base exception for dev-toolkit-39."""
    pass

class ConfigurationError(DevToolkitError):
    """Raised when config validation fails."""
    pass

class ProcessingError(DevToolkitError):
    """Raised during core logic execution failure."""
    pass

class ValidationError(DevToolkitError):
    """Raised when input data is invalid."""
    pass

def handle_toolkit_exception(e: Exception) -> str:
    """Maps internal exceptions to user-friendly error messages."""
    if isinstance(e, ConfigurationError):
        return f"Configuration issue detected: {e}"
    if isinstance(e, ValidationError):
        return f"Invalid data input: {e}"
    if isinstance(e, ProcessingError):
        return f"System processing failure: {e}"
    return "An unexpected internal error occurred."

def safe_execute(func, *args, **kwargs):
    """Wrapper to catch and handle toolkit-specific exceptions."""
    try:
        return func(*args, **kwargs)
    except DevToolkitError as e:
        error_msg = handle_toolkit_exception(e)
        print(f"[ERROR] {error_msg}")
        return None
    except Exception as e:
        print(f"[CRITICAL] Unexpected error: {str(e)}")
        raise