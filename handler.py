import re
from typing import Any, Dict, Generator, List, Union


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into single-level keys with separators."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def batch_items(iterable: List[Any], batch_size: int) -> Generator[List[Any], None, None]:
    """Yield successive batches of a specified size from an iterable list."""
    if batch_size <= 0:
        raise ValueError("batch_size must be greater than zero")
    for i in range(0, len(iterable), batch_size):
        yield iterable[i : i + batch_size]


def safe_get(data: Union[Dict, List], path: str, default: Any = None, sep: str = ".") -> Any:
    """Retrieve a value from nested dictionaries or lists using a dot-separated path."""
    keys = path.split(sep)
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key, default)
        elif isinstance(current, list) and key.isdigit():
            idx = int(key)
            current = current[idx] if 0 <= idx < len(current) else default
        else:
            return default
        if current is default:
            break
    return current


def sanitize_string(text: str, replacement: str = "_") -> str:
    """Sanitize a text string for safe key or filename usage."""
    cleaned = re.sub(r'[\\/*?:"<>|]', replacement, text)
    cleaned = re.sub(r"\s+", replacement, cleaned)
    return cleaned.strip(replacement)
