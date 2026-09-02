"""Module for general data handling utilities.
Provides functions for nested dict access, flattening, and merging.
"""

from typing import Any, Dict, List

def get_nested(data: Dict[str, Any], path: List[str], default: Any = None) -> Any:
    """Retrieve a nested value from a dictionary using a list of keys.
    Returns default if any key is missing.
    """
    current = data
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def set_nested(data: Dict[str, Any], path: List[str], value: Any) -> None:
    """Set a value in a nested dictionary, creating parent dictionaries as needed."""
    if not path:
        return
    current = data
    for key in path[:-1]:
        if key not in current or not isinstance(current.get(key), dict):
            current[key] = {}
        current = current[key]
    current[path[-1]] = value

def deep_merge(base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries, with update overriding base."""
    result = base.copy()
    for key, value in update.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten nested dictionary into a single level dict with separator."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def unflatten_dict(flat_dict: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
    """Convert a flattened dictionary back to nested structure."""
    result: Dict[str, Any] = {}
    for key, value in flat_dict.items():
        keys = key.split(sep)
        set_nested(result, keys, value)
    return result

def remove_empty_values(data: Any) -> Any:
    """Recursively remove keys with empty values (None, empty dict/list)."""
    if isinstance(data, dict):
        return {k: remove_empty_values(v) for k, v in data.items() 
                if v not in (None, {}, [])}
    elif isinstance(data, list):
        return [remove_empty_values(item) for item in data if item not in (None, {}, [])]
    else:
        return data

if __name__ == "__main__":
    sample = {"a": {"b": 1, "c": None}, "d": [1, 2, None]}
    print(get_nested(sample, ["a", "b"]))
    flat = flatten_dict(sample)
    print(flat)
    nested = unflatten_dict(flat)
    print(nested)
    merged = deep_merge({"x": 1, "y": {"z": 2}}, {"y": {"w": 3}})
    print(merged)