"""Data handling utilities for dictionary manipulation and transformation."""

from typing import Any, Dict, List, Optional


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into a single-level dictionary.

    Args:
        d: The nested dictionary to flatten.
        parent_key: Prefix for flattened keys.
        sep: Separator used between nested keys.

    Returns:
        A flattened dictionary with combined keys.
    """
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def deep_get(
    d: Dict[str, Any], path: str, default: Optional[Any] = None, sep: str = "."
) -> Any:
    """Safely retrieve a value from a deeply nested dictionary using key path.

    Args:
        d: Target dictionary.
        path: Key path separated by `sep` (e.g., 'user.profile.name').
        default: Fallback value if the key path is not found.
        sep: Key path separator.

    Returns:
        The value at path if found, otherwise `default`.
    """
    keys = path.split(sep)
    current = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current
