import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading configuration from JSON files with fallback defaults."""

    def __init__(self, default_config: Dict[str, Any] = None):
        self.defaults = default_config or {}

    def load(self, filepath: str) -> Dict[str, Any]:
        """Reads config file and merges with internal defaults."""
        if not os.path.exists(filepath):
            return self.defaults.copy()

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
            
            # Create copy of defaults and update with user values
            config = self.defaults.copy()
            config.update(user_config)
            return config
        except (json.JSONDecodeError, IOError):
            return self.defaults.copy()

# Example usage for dev-toolkit-39
if __name__ == "__main__":
    defaults = {"host": "localhost", "port": 8080, "debug": False}
    loader = ConfigLoader(defaults)
    
    current_config = loader.load("config.json")
    print(f"Active configuration: {current_config}")