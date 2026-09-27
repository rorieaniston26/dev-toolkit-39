from typing import Any, Dict, List, Optional


def flatten_dict(
    nested_dict: Dict[str, Any],
    parent_key: str = "",
    sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into a single-level dictionary."""
    items: List[tuple] = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def process_records(
    records: List[Dict[str, Any]],
    drop_nulls: bool = True,
    flatten: bool = True,
    key_prefix: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Process and normalize a list of dictionary records."""
    processed_records = []
    
    for record in records:
        if not isinstance(record, dict):
            continue
            
        current_record = flatten_dict(record) if flatten else record.copy()
        
        if drop_nulls:
            current_record = {
                k: v for k, v in current_record.items()
                if v is not None and v != ""
            }
            
        if key_prefix:
            current_record = {
                f"{key_prefix}{k}": v for k, v in current_record.items()
            }
            
        processed_records.append(current_record)
        
    return processed_records
