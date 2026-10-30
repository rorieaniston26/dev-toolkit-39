import json
import os
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    """Load and parse JSON configuration from file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_json(filepath: str, data: Dict[str, Any]) -> bool:
    """Save dictionary to JSON file with indentation."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def ensure_dir(path: str) -> None:
    """Create directory path if not exists."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieve environment variable with fallback."""
    return os.environ.get(key, default or "")

def format_byte_size(size: int) -> str:
    """Convert bytes to human-readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"