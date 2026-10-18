class DevToolkitError(Exception):
    """Base exception for dev-toolkit-39 operations."""
    pass

class DataValidationError(DevToolkitError):
    """Raised when data fails format requirements."""
    pass

class ProcessingError(DevToolkitError):
    """Raised when data transformation fails."""
    pass

def validate_payload(data: dict, required_keys: list) -> bool:
    """Ensure payload contains all mandatory keys."""
    if not isinstance(data, dict):
        raise DataValidationError("Payload must be a dictionary")
    
    missing = [key for key in required_keys if key not in data]
    if missing:
        raise DataValidationError(f"Missing keys: {', '.join(missing)}")
    return True

def safe_extract(data: dict, key: str, default=None):
    """Extract nested dictionary values safely."""
    try:
        return data.get(key, default)
    except AttributeError:
        raise ProcessingError(f"Invalid data source provided for key {key}")