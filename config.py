import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging application configuration."""

    def __init__(self, defaults: Dict[str, Any]):
        self.config = defaults.copy()

    def load_from_json(self, filepath: str) -> None:
        """Overwrites default config with values from file."""
        if not os.path.exists(filepath):
            return

        with open(filepath, 'r') as f:
            user_config = json.load(f)
            self.config.update(user_config)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value by key."""
        return self.config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        """Return the full configuration dictionary."""
        return self.config

def load_app_config(path: str = "config.json") -> ConfigLoader:
    """Factory helper for initializing config loader."""
    defaults = {
        "port": 8080,
        "host": "localhost",
        "debug": False
    }
    loader = ConfigLoader(defaults)
    loader.load_from_json(path)
    return loader