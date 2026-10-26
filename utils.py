import json
import os
from typing import Any, Optional

def load_json(path: str) -> Optional[dict]:
    """Read and parse a JSON file safely."""
    if not os.path.exists(path):
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_json(path: str, data: Any) -> bool:
    """Serialize data and write to a JSON file."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def ensure_dir(path: str) -> None:
    """Create directory path if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def format_byte_size(size_bytes: int) -> str:
    """Convert bytes to human-readable string."""
    if size_bytes == 0:
        return "0B"
    units = ("B", "KB", "MB", "GB", "TB")
    i = 0
    while size_bytes >= 1024 and i < len(units) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.2f} {units[i]}"