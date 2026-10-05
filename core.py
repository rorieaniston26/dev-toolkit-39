from typing import Any, Dict


def deep_merge(
    dict1: Dict[Any, Any],
    dict2: Dict[Any, Any],
    list_strategy: str = "extend",
) -> Dict[Any, Any]:
    """Recursively merges two dictionaries with custom list merging strategies.

    Strategies for list conflicts:
    - 'extend': elements of list in dict2 are appended to dict1 (default)
    - 'override': list in dict2 replaces list in dict1
    - 'preserve': list in dict1 is kept, dict2 list is ignored
    """
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Both inputs must be dictionaries")

    merged = dict1.copy()

    for key, value in dict2.items():
        if key in merged:
            node1 = merged[key]
            node2 = value

            if isinstance(node1, dict) and isinstance(node2, dict):
                merged[key] = deep_merge(node1, node2, list_strategy)
            elif isinstance(node1, list) and isinstance(node2, list):
                if list_strategy == "extend":
                    merged[key] = node1 + node2
                elif list_strategy == "override":
                    merged[key] = node2
                elif list_strategy == "preserve":
                    merged[key] = node1
                else:
                    raise ValueError(
                        f"Unknown list strategy: {list_strategy}. Use 'extend', 'override', or 'preserve'."
                    )
            else:
                # Scalar override or mismatched types; dict2 takes precedence
                merged[key] = node2
        else:
            merged[key] = value

    return merged
