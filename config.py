import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON config file and merges with defaults."""
    config = defaults.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Config loading error: {e}. Using defaults.")

    return config

if __name__ == '__main__':
    # Example usage for dev-toolkit-39
    default_settings = {
        "host": "localhost",
        "port": 8080,
        "debug": False
    }
    
    current_config = load_config('settings.json', default_settings)
    print(f"Active configuration: {current_config}")