class DevToolkitError(Exception):
    """Base exception for dev-toolkit-39 operations."""
    pass

class ConfigurationError(DevToolkitError):
    """Raised when environment configuration is missing or invalid."""
    pass

class ProcessingError(DevToolkitError):
    """Raised when data transformation fails."""
    pass

class ValidationError(DevToolkitError):
    """Raised when input validation fails constraints."""
    pass

def handle_exception(e: Exception) -> dict:
    """Standardized response format for toolkit errors."""
    error_type = type(e).__name__
    return {
        "status": "error",
        "error_code": error_type,
        "message": str(e),
        "success": False
    }

# Default error thresholds for operations
MAX_RETRY_ATTEMPTS = 3
TIMEOUT_SECONDS = 30