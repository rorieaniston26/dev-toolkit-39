"""Constants module for dev-toolkit-39.

This module centralizes all configuration constants and magic numbers
to improve maintainability after code cleanup.
"""

from enum import Enum

# Project information
PROJECT_NAME: str = "dev-toolkit-39"
VERSION: str = "1.2.0"
DESCRIPTION: str = "General purpose developer toolkit"

# File system constants
TEMP_DIR: str = "/tmp/dev_toolkit"
LOG_FILE_NAME: str = "toolkit.log"
CONFIG_FILE_NAME: str = "config.json"

# Processing limits
MAX_LINES_PER_FILE: int = 10000
CHUNK_SIZE: int = 4096
MAX_CONCURRENT_TASKS: int = 4

# Validation patterns
VALID_EMAIL_PATTERN: str = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Timeouts and retries
REQUEST_TIMEOUT: int = 30  # seconds
MAX_RETRIES: int = 3
RETRY_DELAY: float = 1.0  # seconds

# Status codes
class StatusCode(Enum):
    """Status codes for operations."""
    SUCCESS = 0
    WARNING = 1
    ERROR = 2
    CRITICAL = 3

# Default configuration
DEFAULT_CONFIG: dict = {
    "log_level": "INFO",
    "output_format": "text",
    "enable_debug": False,
    "max_workers": 2,
}

# Helper to get all constants
def get_all_constants() -> dict:
    """Return a dictionary of all public constants."""
    return {
        "project_name": PROJECT_NAME,
        "version": VERSION,
        "description": DESCRIPTION,
        "temp_dir": TEMP_DIR,
        "log_file_name": LOG_FILE_NAME,
        "config_file_name": CONFIG_FILE_NAME,
        "max_lines_per_file": MAX_LINES_PER_FILE,
        "chunk_size": CHUNK_SIZE,
        "max_concurrent_tasks": MAX_CONCURRENT_TASKS,
        "request_timeout": REQUEST_TIMEOUT,
        "max_retries": MAX_RETRIES,
        "retry_delay": RETRY_DELAY,
        "default_config": DEFAULT_CONFIG,
    }

# Example usage in module
if __name__ == "__main__":
    print(f"Loaded {PROJECT_NAME} v{VERSION}")
    print("Constants available:", list(get_all_constants().keys()))