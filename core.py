from typing import Any, Dict, List, Tuple


class ValidationError(Exception):
    """Raised when input payload fails validation rules."""
    pass


def validate_item(item: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate an individual processing item schema and contents."""
    if not isinstance(item, dict):
        return False, "Payload must be a dictionary"

    if "id" not in item or not isinstance(item["id"], (int, str)):
        return False, "Missing or invalid 'id' field"

    if "action" not in item or not isinstance(item["action"], str):
        return False, "Missing or invalid 'action' string"

    allowed_actions = {"parse", "transform", "format", "clean"}
    if item["action"].lower() not in allowed_actions:
        return False, f"Action '{item['action']}' not in supported set: {allowed_actions}"

    return True, ""


def process_batch(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Main processing loop with input validation on each iteration."""
    summary = {"successful": 0, "skipped": 0, "errors": []}

    for index, task in enumerate(tasks):
        is_valid, error_msg = validate_item(task)
        if not is_valid:
            summary["skipped"] += 1
            summary["errors"].append({"index": index, "reason": error_msg})
            continue

        # Execute action on validated task
        action = task["action"].lower()
        task_id = task["id"]
        payload = task.get("data", "")

        if action == "clean":
            payload = str(payload).strip()
        elif action == "format":
            payload = str(payload).upper()

        summary["successful"] += 1

    return summary
