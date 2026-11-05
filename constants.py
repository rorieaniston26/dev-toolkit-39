import enum
from typing import Final

# general constants for dev-toolkit-39

class DataFormat(enum.Enum):
    JSON = "json"
    CSV = "csv"
    YAML = "yaml"
    XML = "xml"

# system configurations
DEFAULT_ENCODING: Final[str] = "utf-8"
CHUNK_SIZE: Final[int] = 4096
MAX_RETRIES: Final[int] = 3

# status codes mapping
STATUS_SUCCESS: Final[int] = 200
STATUS_BAD_REQUEST: Final[int] = 400
STATUS_SERVER_ERROR: Final[int] = 500

# environment constraints
ALLOWED_EXTENSIONS: Final[set[str]] = {".json", ".csv", ".txt"}

def get_timeout_value(priority: str = "normal") -> int:
    """returns operation timeout based on priority level"""
    timeouts = {
        "low": 60,
        "normal": 30,
        "high": 10
    }
    return timeouts.get(priority, 30)

# validation patterns
EMAIL_REGEX: Final[str] = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"