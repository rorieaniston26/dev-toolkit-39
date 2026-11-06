import json
from typing import Any, Dict, Optional

def clean_dict_keys(data: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively strip whitespace from dictionary keys."""
    cleaned = {}
    for key, value in data.items():
        new_key = str(key).strip()
        if isinstance(value, dict):
            cleaned[new_key] = clean_dict_keys(value)
        elif isinstance(value, list):
            cleaned[new_key] = [clean_dict_keys(i) if isinstance(i, dict) else i for i in value]
        else:
            cleaned[new_key] = value
    return cleaned

def safe_json_load(file_path: str, default: Optional[Dict] = None) -> Dict[str, Any]:
    """Attempt to parse JSON file with fallback."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default or {}

def flatten_data(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten nested dictionary structure for flat storage."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_data(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)