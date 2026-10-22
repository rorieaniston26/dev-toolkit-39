import json
import os
from typing import Any, Dict

def load_config(config_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration with fallback to defaults."""
    config = defaults.copy()

    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(config_path: str, config: Dict[str, Any]) -> None:
    """Persists configuration dictionary to file."""
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)

if __name__ == '__main__':
    # Example usage for dev-toolkit-39
    default_settings = {"debug": False, "port": 8080}
    settings = load_config('settings.json', default_settings)
    print(f"Active settings: {settings}")