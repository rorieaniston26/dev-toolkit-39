"""General utility helpers for data manipulation and structure reorganization."""

from typing import Any, Dict, Generator, List, TypeVar

T = TypeVar("T")


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into single-level key paths."""
    items: List[tuple[str, Any]] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def chunk_iterable(
    items: List[T], size: int
) -> Generator[List[T], None, None]:
    """Yield successive chunks of specified size from a list."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    for i in range(0, len(items), size):
        yield items[i : i + size]


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries into a new single dictionary."""
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def sanitize_dict_keys(
    data: Dict[str, Any], lowercase: bool = True
) -> Dict[str, Any]:
    """Normalize dictionary keys by stripping whitespace and standardizing case."""
    cleaned = {}
    for key, val in data.items():
        new_key = key.strip().lower() if lowercase else key.strip()
        if isinstance(val, dict):
            cleaned[new_key] = sanitize_dict_keys(val, lowercase=lowercase)
        else:
            cleaned[new_key] = val
    return cleaned
