from typing import Any, Dict, List

def flatten_nested_dict(data: Dict[str, Any], separator: str = '.') -> Dict[str, Any]:
    """
    Flatten a nested dictionary into a single level dictionary.
    Keys are joined with the separator.
    """
    def _flatten(current: Dict[str, Any], parent: str = '') -> Dict[str, Any]:
        items = {}
        for key, value in current.items():
            new_key = f"{parent}{separator}{key}" if parent else key
            if isinstance(value, dict):
                items.update(_flatten(value, new_key))
            else:
                items[new_key] = value
        return items
    return _flatten(data)

def merge_data_sources(source1: Dict[str, Any], source2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively merge two data dictionaries.
    Values from source2 take precedence.
    """
    result = source1.copy()
    for key, value in source2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_data_sources(result[key], value)
        else:
            result[key] = value
    return result

def split_into_chunks(items: List[Any], size: int) -> List[List[Any]]:
    """
    Divide a list into smaller chunks of given size.
    """
    if size < 1:
        raise ValueError('Size must be at least 1')
    return [items[i:i + size] for i in range(0, len(items), size)]

def extract_values(data: List[Dict[str, Any]], key: str) -> List[Any]:
    """
    Extract values for a specific key from list of dictionaries.
    """
    return [item[key] for item in data if key in item]

def safe_get(data: Dict[str, Any], path: str, default: Any = None, separator: str = '.') -> Any:
    """
    Safely retrieve a value from nested dict using dot notation path.
    """
    keys = path.split(separator)
    current = data
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            return default
    return current