import os
from typing import Final

# Application environment settings
ENV: Final[str] = os.getenv('APP_ENV', 'development')
DEBUG: Final[bool] = os.getenv('DEBUG', 'false').lower() == 'true'

# Path definitions for core directories
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
DATA_DIR: Final[str] = os.path.join(BASE_DIR, 'data')
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Timeouts and network thresholds
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Formatting constants
DATE_FORMAT: Final[str] = '%Y-%m-%d %H:%M:%S'
DEFAULT_ENCODING: Final[str] = 'utf-8'

# Resource limits
MAX_WORKER_THREADS: Final[int] = 8
BATCH_SIZE: Final[int] = 100

def get_config_summary() -> dict:
    """Returns a summary of active configuration constants."""
    return {
        'env': ENV,
        'debug': DEBUG,
        'timeout': DEFAULT_TIMEOUT,
        'retries': MAX_RETRIES
    }