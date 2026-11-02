from typing import Final, Dict, List

# Configuration constants for dev-toolkit-39
APP_NAME: Final[str] = "dev-toolkit-39"
VERSION: Final[str] = "1.0.0"

# Default operation timeouts in seconds
TIMEOUT_DEFAULT: Final[int] = 30
TIMEOUT_EXTENDED: Final[int] = 300

# Supported environment mapping
ENV_MAP: Final[Dict[str, str]] = {
    "dev": "development",
    "stg": "staging",
    "prd": "production"
}

# Reserved keyword exclusion list
RESERVED_KEYWORDS: Final[List[str]] = [
    "root",
    "admin",
    "system",
    "null"
]

def get_app_metadata() -> Dict[str, str]:
    """Retrieve standard toolkit metadata dictionary."""
    return {
        "name": APP_NAME,
        "version": VERSION
    }