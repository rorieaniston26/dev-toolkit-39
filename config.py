import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging application configuration."""

    def __init__(self, defaults: Dict[str, Any]):
        self.config = defaults.copy()

    def load_from_file(self, filepath: str) -> None:
        """Overwrites defaults with values from a JSON file."""
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)

    def load_from_env(self, prefix: str = 'APP_') -> None:
        """Updates config from environment variables matching prefix."""
        for key in self.config.keys():
            env_key = f"{prefix}{key.upper()}"
            value = os.getenv(env_key)
            if value is not None:
                self.config[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves config value by key."""
        return self.config.get(key, default)

# Example usage initialization
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    loader = ConfigLoader(defaults)
    loader.load_from_file('config.json')
    loader.load_from_env()