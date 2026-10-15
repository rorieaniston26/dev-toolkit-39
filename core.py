from typing import Any, Dict, List, Optional
import json

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single level structure.
    """
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def safe_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """
    Retrieves a nested value from a dictionary using dot notation.
    """
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default

def filter_by_keys(data: List[Dict[str, Any]], keys: List[str]) -> List[Dict[str, Any]]:
    """
    Returns a list of dictionaries containing only the specified keys.
    """
    return [{k: item[k] for k in keys if k in item} for item in data]

def serialize_to_json(data: Any) -> str:
    """
    Converts data to a JSON string with consistent formatting.
    """
    return json.dumps(data, indent=4, sort_keys=True)