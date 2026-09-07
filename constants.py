import logging
from enum import Enum
from typing import Final

# Application-wide status codes and environment keys
class AppStatus(Enum):
    SUCCESS = 0
    ERR_MISSING_CONFIG = 1
    ERR_INVALID_INPUT = 2
    ERR_CONNECTION_TIMEOUT = 3
    ERR_UNKNOWN = 99

# Configuration default limits
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Log configuration setup
LOG_FORMAT: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL: Final[int] = logging.INFO

# Error message mapping for graceful handling
ERROR_MESSAGES: Final[dict] = {
    AppStatus.ERR_MISSING_CONFIG.value: "Critical environment variables missing",
    AppStatus.ERR_INVALID_INPUT.value: "Input data violates schema requirements",
    AppStatus.ERR_CONNECTION_TIMEOUT.value: "Network request exceeded allotted time",
    AppStatus.ERR_UNKNOWN.value: "An unhandled exception occurred during execution"
}

def get_error_message(status_code: int) -> str:
    """Retrieve standardized error string for status codes."""
    return ERROR_MESSAGES.get(status_code, "Unexpected system error")

if __name__ == "__main__":
    # Validation check for defined constant constraints
    assert DEFAULT_TIMEOUT > 0, "Timeout must be positive"
    print("Constants module initialized successfully.")