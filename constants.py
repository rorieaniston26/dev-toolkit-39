"""Centralized constants and configuration defaults for dev-toolkit-39."""

import re
from enum import Enum
from typing import Final

# System identity metadata
APP_NAME: Final[str] = "dev-toolkit-39"
APP_VERSION: Final[str] = "1.4.0"

# Network operation defaults
DEFAULT_TIMEOUT: Final[float] = 30.0
CONNECT_TIMEOUT: Final[float] = 5.0
MAX_RETRIES: Final[int] = 3
BACKOFF_FACTOR: Final[float] = 1.5

# Processing and storage limits
DEFAULT_BUFFER_SIZE: Final[int] = 8192
MAX_FILE_SIZE_BYTES: Final[int] = 104_857_600  # 100 MB
ALLOWED_TEXT_ENCODINGS: Final[tuple[str, ...]] = ("utf-8", "ascii", "latin-1")

# Pre-compiled validation patterns
EMAIL_REGEX: Final[re.Pattern] = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)
SLUG_REGEX: Final[re.Pattern] = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_REGEX: Final[re.Pattern] = re.compile(r"^\d+\.\d+\.\d+$")


class Environment(str, Enum):
    """Supported runtime execution environments."""
    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"


class ExitCode:
    """Standard application exit status codes."""
    SUCCESS: Final[int] = 0
    ERROR_GENERAL: Final[int] = 1
    ERROR_INVALID_USAGE: Final[int] = 2
    ERROR_CONFIG: Final[int] = 3
    ERROR_TIMEOUT: Final[int] = 4
