import os
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

def load_config_value(key: str, default: Any = None) -> Any:
    """Retrieves environment configuration with type-safe fallback."""
    try:
        value = os.environ.get(key)
        if value is None:
            if default is None:
                raise KeyError(f"Missing required configuration: {key}")
            return default
        return value
    except Exception as e:
        logger.error(f"Unexpected error reading configuration {key}: {e}")
        return default

def validate_config_schema(config: Dict[str, Any], required_keys: list) -> bool:
    """Checks configuration integrity against required keys."""
    try:
        if not isinstance(config, dict):
            raise ValueError("Configuration must be a dictionary")
        
        missing = [k for k in required_keys if k not in config]
        if missing:
            logger.warning(f"Configuration missing keys: {', '.join(missing)}")
            return False
        return True
    except Exception as e:
        logger.error(f"Schema validation failed: {e}")
        return False

# Default application settings
APP_SETTINGS = {
    "env": load_config_value("APP_ENV", "development"),
    "timeout": int(load_config_value("APP_TIMEOUT", 30)),
    "debug": load_config_value("DEBUG", "false").lower() == "true"
}