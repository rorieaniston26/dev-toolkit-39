class DevToolkitError(Exception):
    """Base exception class for dev-toolkit-39."""
    pass

class DataValidationError(DevToolkitError):
    """Raised when data fails validation schema."""
    pass

class ProcessingError(DevToolkitError):
    """Raised when data transformation fails."""
    pass

def validate_data_type(data, expected_type):
    """Utility to enforce type consistency in pipelines."""
    if not isinstance(data, expected_type):
        raise DataValidationError(f"Expected {expected_type.__name__}, got {type(data).__name__}")
    return True

def safe_process(func, data):
    """Wrapper to handle common data processing faults."""
    try:
        return func(data)
    except Exception as e:
        raise ProcessingError(f"Failed to process data: {str(e)}") from e

if __name__ == '__main__':
    # Example usage demonstration
    try:
        validate_data_type("test", int)
    except DataValidationError:
        pass