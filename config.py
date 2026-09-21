import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging application configurations."""

    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_file(self, filepath: str) -> None:
        """Updates internal config with values from JSON file."""
        if not os.path.exists(filepath):
            return

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                self._deep_merge(self.config, user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Configuration error: {e}")

    def _deep_merge(self, base: Dict[str, Any], overrides: Dict[str, Any]) -> None:
        """Recursively merges dictionary overrides into base config."""
        for key, value in overrides.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._deep_merge(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves config value by key."""
        return self.config.get(key, default)

# Usage example
if __name__ == '__main__':
    defaults = {"port": 8080, "debug": False, "db": {"host": "localhost"}}
    loader = ConfigLoader(defaults)
    loader.load_from_file("config.json")
    print(f"Active port: {loader.get('port')}")