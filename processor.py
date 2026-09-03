from typing import Any, Dict, List


class ValidationError(Exception):
    """Custom exception for payload validation failures."""
    pass


def validate_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that incoming data contains required keys and valid types."""
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a dictionary")

    required_keys = ["task_id", "command", "params"]
    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required field: {key}")

    if not isinstance(data["task_id"], (int, str)) or not str(data["task_id"]).strip():
        raise ValidationError("Field 'task_id' must be a non-empty string or int")

    if not isinstance(data["params"], dict):
        raise ValidationError("Field 'params' must be a dictionary")

    return data


def process_batch(batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Main processing loop with per-item input validation."""
    results = []

    for index, item in enumerate(batch):
        try:
            valid_data = validate_payload(item)
            results.append({
                "task_id": valid_data["task_id"],
                "status": "processed",
                "command": valid_data["command"]
            })
        except ValidationError as err:
            results.append({
                "index": index,
                "status": "failed",
                "error": str(err)
            })

    return results
