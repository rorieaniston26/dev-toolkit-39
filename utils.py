import math
from typing import Any, Dict, Generator, List


def chunk_list(data: List[Any], size: int) -> Generator[List[Any], None, None]:
    """Split a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    for i in range(0, len(data), size):
        yield data[i : i + size]


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "_"
) -> Dict[str, Any]:
    """Flatten a nested dictionary, joining keys with a separator."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def merge_dicts(*dicts: Dict[Any, Any]) -> Dict[Any, Any]:
    """Deep merge multiple dictionaries sequentially."""
    result: Dict[Any, Any] = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            if (
                key in result
                and isinstance(result[key], dict)
                and isinstance(value, dict)
            ):
                result[key] = merge_dicts(result[key], value)
            else:
                result[key] = value
    return result


def format_bytes(size_in_bytes: int) -> str:
    """Convert a byte count into a human-readable string representation."""
    if size_in_bytes < 0:
        raise ValueError("Size cannot be negative.")
    if size_in_bytes == 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = int(math.floor(math.log(size_in_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_in_bytes / p, 2)
    return f"{s} {units[i]}"
