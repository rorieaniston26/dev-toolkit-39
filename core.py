import json
import os
from typing import Any, Dict

def load_json(filepath: str) -> Dict[str, Any]:
    """Load and parse JSON file content."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath: str, data: Dict[str, Any]) -> None:
    """Write data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def flatten_dict(data: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flatten nested dictionaries recursively."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_env_var(key: str, default: Any = None) -> Any:
    """Access environment variables with defaults."""
    return os.getenv(key, default)

def slugify(text: str) -> str:
    """Transform strings into URL-safe formats."""
    return text.lower().replace(' ', '-').replace('_', '-')