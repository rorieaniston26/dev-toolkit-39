from typing import Any, Dict, Generator, List

def deep_merge(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merges dict2 into dict1, returning a new dictionary."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def get_by_path(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieves a nested value from a dictionary using a dot-separated path."""
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def chunk_list(data: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """Yields successive chunks of a list based on specified size."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]
