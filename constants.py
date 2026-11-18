import logging
from typing import Final, Dict, Any

# Application-wide configuration and constraints
MAX_RETRIES: Final[int] = 3
TIMEOUT_SECONDS: Final[int] = 30
DEFAULT_ENCODING: Final[str] = 'utf-8'

# Error handling constants for service resilience
RETRYABLE_STATUS_CODES: Final[set] = {500, 502, 503, 504}

# Logging format consistency
LOG_FORMAT: Final[str] = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def get_app_settings() -> Dict[str, Any]:
    """Retrieve read-only application settings map."""
    return {
        "max_retries": MAX_RETRIES,
        "timeout": TIMEOUT_SECONDS,
        "encoding": DEFAULT_ENCODING,
        "retryable": list(RETRYABLE_STATUS_CODES)
    }

# Validation of runtime environment integrity
def validate_constants() -> bool:
    """
    Verify that critical constant values meet
    operational thresholds before application startup.
    """
    if MAX_RETRIES < 0:
        logging.error("invalid retry configuration detected")
        return False
    if TIMEOUT_SECONDS <= 0:
        logging.error("invalid timeout configuration detected")
        return False
    return True