import os
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def load_config_value(key: str, default: Any = None) -> Any:
    """Retrieves environment configuration with type-safe defaults."""
    try:
        value = os.getenv(key)
        if value is None:
            return default
        return value
    except Exception as e:
        logger.error(f"Unexpected error accessing env var {key}: {e}")
        return default

def parse_int_config(key: str, default: int) -> int:
    """Parses environment variable to integer with error resilience."""
    raw_value = os.getenv(key)
    if raw_value is None:
        return default
    try:
        return int(raw_value)
    except (ValueError, TypeError):
        logger.warning(f"Invalid integer for {key}: {raw_value}. Using default: {default}")
        return default

def get_app_settings() -> Dict[str, Any]:
    """Aggregates settings from environment variables."""
    return {
        "PORT": parse_int_config("APP_PORT", 8080),
        "DEBUG": load_config_value("DEBUG_MODE", "false").lower() == "true",
        "TIMEOUT": parse_int_config("REQUEST_TIMEOUT", 30)
    }