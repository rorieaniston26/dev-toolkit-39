from typing import Any, Dict, List, Optional, Sequence, TypeVar

T = TypeVar("T")


def chunk_list(items: Sequence[T], chunk_size: int) -> List[List[T]]:
    """Split a sequence into fixed-size chunks.

    Args:
        items: Sequence of elements to be split.
        chunk_size: Maximum size of each chunk. Must be positive.

    Returns:
        List of chunks containing items from the original sequence.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    return [list(items[i : i + chunk_size]) for i in range(0, len(items), chunk_size)]


def deep_merge_dicts(
    dict1: Dict[str, Any], dict2: Dict[str, Any]
) -> Dict[str, Any]:
    """Recursively merge two dictionaries into a new dictionary.

    Args:
        dict1: Base dictionary.
        dict2: Dictionary with overrides and additions.

    Returns:
        A new nested dictionary containing merged key-value pairs.
    """
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def safe_int_cast(val: Any, default: Optional[int] = None) -> Optional[int]:
    """Attempt to cast a value to an integer safely.

    Args:
        val: Any value to cast to integer.
        default: Fallback value if conversion fails.

    Returns:
        Converted integer or default value.
    """
    try:
        return int(val)
    except (ValueError, TypeError):
        return default
