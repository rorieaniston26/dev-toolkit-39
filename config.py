import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON config file and merges with provided defaults."""
    config = defaults.copy()

    if not os.path.exists(path):
        return config

    try:
        with open(path, 'r') as f:
            user_data = json.load(f)
            config.update(user_data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def get_env_config(prefix: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Overrides defaults with matching environment variables."""
    config = defaults.copy()
    for key in config.keys():
        env_key = f"{prefix}_{key.upper()}"
        if env_key in os.environ:
            config[key] = os.environ[env_key]
    return config