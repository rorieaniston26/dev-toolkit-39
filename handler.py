import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class DataProcessingError(Exception):
    """Custom exception for handler failures."""
    pass

def safe_process(data: Any) -> Optional[dict]:
    """
    Safely processes input data with exhaustive error checks.
    Returns a dict on success, None on failure.
    """
    if not data:
        logger.warning("received empty input data")
        return None

    try:
        if not isinstance(data, dict):
            raise ValueError(f"expected dict, got {type(data).__name__}")
        
        # Simulation of core processing logic
        result = {
            "id": data.get("id"),
            "status": "processed",
            "content": data.get("payload", "").strip()
        }

        if not result["id"]:
            raise DataProcessingError("missing required field: id")
            
        return result

    except (ValueError, KeyError) as e:
        logger.error(f"validation error in input: {e}")
    except DataProcessingError as e:
        logger.error(f"business logic violation: {e}")
    except Exception as e:
        logger.critical(f"unexpected system error: {e}", exc_info=True)
    
    return None