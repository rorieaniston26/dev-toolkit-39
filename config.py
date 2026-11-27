import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_file(self, file_path: str) -> None:
        """Updates internal config from a JSON file."""
        if not os.path.exists(file_path):
            return

        try:
            with open(file_path, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves config value by key."""
        return self.config.get(key, default)

def create_config(defaults: Dict[str, Any], path: str = 'config.json') -> ConfigLoader:
    """Factory for config loader initialization."""
    loader = ConfigLoader(defaults)
    loader.load_from_file(path)
    return loader