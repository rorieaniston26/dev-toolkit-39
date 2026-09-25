class ToolkitError(Exception):
    """Base exception for all dev-toolkit-39 errors."""
    pass

class ConfigurationError(ToolkitError):
    """Raised when config files are missing or malformed."""
    pass

class ProcessingError(ToolkitError):
    """Raised during core logic execution failures."""
    pass

class ValidationError(ToolkitError):
    """Raised when input data fails validation checks."""
    pass

def handle_toolkit_exception(e: Exception) -> None:
    """Centralized error reporting for toolkit components."""
    if isinstance(e, ToolkitError):
        print(f"[Toolkit Error] {type(e).__name__}: {e}")
    else:
        print(f"[Unexpected Error] {type(e).__name__}: {e}")

if __name__ == "__main__":
    try:
        raise ConfigurationError("Missing config.yaml file")
    except ToolkitError as err:
        handle_toolkit_exception(err)