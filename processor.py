from typing import Any, Dict, List, Tuple


class ValidationError(Exception):
    """Custom exception for data validation failures."""
    pass


def validate_input_record(record: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate single record structure and field constraints."""
    if not isinstance(record, dict):
        return False, "Record must be a dictionary"

    if "id" not in record or not record["id"]:
        return False, "Missing or empty mandatory 'id' field"

    if "command" not in record or not isinstance(record["command"], str):
        return False, "Field 'command' must be a valid string"

    if not record["command"].strip():
        return False, "Field 'command' cannot be blank"

    return True, "OK"


def run_processing_loop(batch: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Execute processing loop with strict input validation."""
    success_count = 0
    error_count = 0
    results: List[Dict[str, Any]] = []

    for record in batch:
        is_valid, message = validate_input_record(record)
        if not is_valid:
            error_count += 1
            results.append({"status": "rejected", "reason": message, "data": record})
            continue

        # Process valid records
        cmd = record["command"].strip().lower()
        results.append({
            "id": record["id"],
            "status": "completed",
            "action_taken": f"executed_{cmd}"
        })
        success_count += 1

    return {
        "processed": success_count,
        "rejected": error_count,
        "details": results
    }
