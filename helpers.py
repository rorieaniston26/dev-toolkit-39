import json
import os
from datetime import datetime
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    """Load and parse a JSON file safely."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], filepath: str) -> None:
    """Serialize data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_timestamp() -> str:
    """Return current ISO formatted timestamp."""
    return datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def ensure_dir(path: str) -> None:
    """Create directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def format_byte_size(size_bytes: int) -> str:
    """Human readable byte conversion."""
    if size_bytes == 0:
        return '0B'
    units = ("B", "KB", "MB", "GB", "TB")
    i = 0
    while size_bytes >= 1024 and i < len(units) - 1:
        size_bytes /= 1024
        i += 1
    return f"{size_bytes:.2f} {units[i]}"