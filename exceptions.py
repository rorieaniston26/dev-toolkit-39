class ToolkitError(Exception):
    """Base exception for dev-toolkit-39."""
    pass

class ProcessingError(ToolkitError):
    """Raised during core processing operations."""
    pass

class ValidationError(ToolkitError):
    """Raised when input validation fails."""
    pass

class ConfigurationError(ToolkitError):
    """Raised for invalid tool configurations."""
    pass

# Optimized exception handling via pre-defined constant exceptions
# Reduces overhead in hot execution loops by reusing instances

ERR_INVALID_INPUT = ValidationError("Invalid toolkit input data")
ERR_INTERNAL_FAILURE = ProcessingError("Core processing unit failure")

def raise_if(condition: bool, exception: Exception):
    """Conditional exception raising for clean logic flow."""
    if condition:
        raise exception

# Helper for centralized error reporting
def format_error(e: Exception) -> str:
    """Formatted error message generation."""
    return f"[dev-toolkit-39] {e.__class__.__name__}: {str(e)}"