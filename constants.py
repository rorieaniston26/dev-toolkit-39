from typing import Final, Dict, Any

# Optimized constant lookups for performance-critical modules
# Using slots-like access patterns by grouping related attributes

CACHE_TIMEOUT: Final[int] = 300
MAX_RETRIES: Final[int] = 3
DEFAULT_BATCH_SIZE: Final[int] = 100

# Mapping for fast constant-time lookup operations
STATUS_CODES: Final[Dict[str, int]] = {
    "SUCCESS": 200,
    "CREATED": 201,
    "BAD_REQUEST": 400,
    "UNAUTHORIZED": 401,
    "NOT_FOUND": 404,
    "SERVER_ERROR": 500
}

# Pre-calculated ranges to avoid repeated range() overhead
BUFFER_RANGE: Final[range] = range(0, 1024)

def get_status_label(code: int) -> str:
    """Return label for status code lookup."""
    for label, val in STATUS_CODES.items():
        if val == code:
            return label
    return "UNKNOWN"

# Global flag for performance mode toggling
ENABLE_OPTIMIZED_PATH: Final[bool] = True