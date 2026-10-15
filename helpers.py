import json
import os
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Optional[Dict[str, Any]]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_json(filepath: str, data: Dict[str, Any]) -> bool:
    """Serializes dictionary to a JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def ensure_directory(path: str) -> None:
    """Creates target directory if missing."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_env_var(key: str, default: Any = None) -> Any:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default)

def sanitize_string(value: str) -> str:
    """Removes non-alphanumeric chars from string."""
    return ''.join(c for c in value if c.isalnum())