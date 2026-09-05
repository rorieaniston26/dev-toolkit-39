class ToolkitError(Exception):
    """Base exception for dev-toolkit-39 operations."""
    pass

class DataProcessingError(ToolkitError):
    """Raised when data transformation or validation fails."""
    pass

class ConfigurationError(ToolkitError):
    """Raised when environment or settings are invalid."""
    pass

def handle_data_integrity(data, required_fields):
    """Validate that a dictionary contains all mandatory keys."""
    if not isinstance(data, dict):
        raise DataProcessingError("Input must be a dictionary")
    
    missing = [f for f in required_fields if f not in data]
    if missing:
        raise DataProcessingError(f"Missing required fields: {', '.join(missing)}")
    
    return True

def safe_extract(data, key, default=None):
    """Safely retrieve value from dict or return default."""
    try:
        return data.get(key, default)
    except AttributeError:
        raise DataProcessingError(f"Invalid data source provided: {type(data)}")