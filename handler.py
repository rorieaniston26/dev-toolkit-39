import json
from typing import Any, Dict, Optional

def safe_data_load(data: str, default: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Parses input string as JSON with fallback to default.
    Returns empty dictionary if parsing fails.
    """
    if default is None:
        default = {}

    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return default

def flatten_dict(nested_data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single-level dictionary.
    Uses recursive approach with underscore separation.
    """
    items = []
    for k, v in nested_data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_payload(data: Dict[str, Any], allowed_keys: list) -> Dict[str, Any]:
    """
    Filters dictionary to keep only specified keys.
    Useful for clean API output.
    """
    return {k: v for k, v in data.items() if k in allowed_keys}