import os
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class ConfigLoader:
    """Handles loading and validation of application configurations."""

    @staticmethod
    def get_env_var(key: str, default: Optional[str] = None) -> str:
        """Retrieves environment variable with error checking."""
        try:
            value = os.getenv(key, default)
            if value is None:
                raise ValueError(f"Missing required configuration: {key}")
            return value
        except Exception as e:
            logger.error(f"Configuration retrieval error for {key}: {e}")
            raise

    def load_database_config(self) -> Dict[str, Any]:
        """Parses database settings with edge case validation."""
        try:
            db_url = self.get_env_var("DB_URL")
            timeout_str = self.get_env_var("DB_TIMEOUT", "30")
            
            if not timeout_str.isdigit():
                logger.warning("Invalid timeout format, defaulting to 30")
                timeout = 30
            else:
                timeout = int(timeout_str)

            return {
                "url": db_url,
                "timeout": timeout,
                "pool_size": int(self.get_env_var("DB_POOL_SIZE", "5"))
            }
        except (ValueError, TypeError) as e:
            logger.critical(f"Critical database configuration failure: {e}")
            return {}

# Instantiate helper for project-wide use
config = ConfigLoader()