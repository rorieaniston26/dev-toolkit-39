import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging application configuration."""

    def __init__(self, defaults: Dict[str, Any] = None):
        self.config = defaults or {}

    def load_from_file(self, file_path: str) -> None:
        """Updates config dictionary from a JSON file."""
        if not os.path.exists(file_path):
            return
        
        try:
            with open(file_path, 'r') as f:
                file_data = json.load(f)
                self.config.update(file_data)
        except (json.JSONDecodeError, IOError):
            pass

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Overrides config values using environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self.config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves value with fallback mechanism."""
        return self.config.get(key, default)

# Example instantiation
# loader = ConfigLoader(defaults={'port': 8080})
# loader.load_from_file('config.json')
# loader.load_from_env()