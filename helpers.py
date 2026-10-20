import json
import os
from typing import Any, Dict, Optional

def read_json_file(filepath: str) -> Dict[str, Any]:
    """Reads and parses a JSON file safely."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def write_json_file(filepath: str, data: Dict[str, Any]) -> bool:
    """Writes data to a JSON file with indentation."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default or '')

def slugify(text: str) -> str:
    """Converts string to a URL-friendly format."""
    return '-'.join(text.lower().split()).replace(' ', '-')

def ensure_directory(path: str) -> None:
    """Creates directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
