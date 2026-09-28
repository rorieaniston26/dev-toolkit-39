import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

# Configure standard logger for project
logger = logging.getLogger('dev-toolkit-39')

def load_json(filepath: str) -> Optional[Dict[str, Any]]:
    """Parses a json file into a python dictionary."""
    path = Path(filepath)
    if not path.exists():
        logger.error(f'file not found: {filepath}')
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f'invalid json format: {e}')
        return None

def safe_get(data: Dict, key: str, default: Any = None) -> Any:
    """Safely retrieves a value from a nested dictionary structure."""
    keys = key.split('.')
    current = data
    try:
        for k in keys:
            current = current[k]
        return current
    except (KeyError, TypeError):
        return default

def ensure_dir(path: str) -> None:
    """Creates a directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)

def format_byte_size(size_bytes: int) -> str:
    """Converts bytes into a human-readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f'{size_bytes:.2f} {unit}'
        size_bytes /= 1024.0
    return f'{size_bytes:.2f} TB'