from typing import List, Dict, Any, Optional
import json

def format_data(data: Dict[str, Any], indent: int = 4) -> str:
    """Converts a dictionary into a pretty-printed JSON string."""
    return json.dumps(data, indent=indent)

def filter_list_by_key(items: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """Returns a subset of the list matching the specified key-value pair."""
    return [item for item in items if item.get(key) == value]

def merge_configs(base: Dict[str, Any], overrides: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Deeply merges an optional override dictionary into a base configuration."""
    if not overrides:
        return base
    
    result = base.copy()
    for key, value in overrides.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result

def get_nested_value(data: Dict[str, Any], path: List[str], default: Any = None) -> Any:
    """Retrieves a value from a nested dictionary using a list of keys."""
    current = data
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current