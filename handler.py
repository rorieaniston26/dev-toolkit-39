import logging
from typing import Any, Optional

# Configure logger for dev-toolkit-39
logger = logging.getLogger('dev-toolkit-39')

class DataProcessingError(Exception):
    """Custom exception for handler failures."""
    pass

def safe_process_input(data: Any) -> Optional[dict]:
    """Processes input data with boundary and type validation."""
    try:
        if data is None:
            raise ValueError("Input data cannot be null")
        
        if not isinstance(data, dict):
            raise TypeError(f"Expected dict, got {type(data).__name__}")

        # Simulate processing logic
        processed_result = {
            "status": "success",
            "payload": data.get("key", "default_value"),
            "metadata": {"size": len(data)}
        }
        
        return processed_result

    except ValueError as ve:
        logger.error(f"Validation error occurred: {ve}")
        return None
    except TypeError as te:
        logger.error(f"Type mismatch error: {te}")
        return None
    except Exception as e:
        logger.critical(f"Unexpected system failure: {str(e)}")
        raise DataProcessingError("Critical failure in handler flow") from e

if __name__ == "__main__":
    # Test case execution for validation
    result = safe_process_input({"key": "value"})
    print(f"Processing result: {result}")