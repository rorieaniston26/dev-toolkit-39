import json
import os
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], filepath: str) -> bool:
    """Writes a dictionary to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback default."""
    return os.getenv(key, default or "")

def chunk_list(data: list, size: int):
    """Generator to split list into chunks of specific size."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def slugify(text: str) -> str:
    """Converts string to a URL-friendly slug format."""
    return "-".join(text.lower().split()).encode('ascii', 'ignore').decode('utf-8')