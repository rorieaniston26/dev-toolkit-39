class ValidationError(ValueError):
    """Exception raised for input validation failures in the processor."""
    pass

def validate_payload(data: dict) -> None:
    """Validates that the incoming payload has the required fields and types."""
    if not isinstance(data, dict):
        raise ValidationError("Input must be a dictionary")
    
    required_keys = ["id", "task", "payload"]
    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required key: {key}")
            
    if not isinstance(data["id"], int) or data["id"] <= 0:
        raise ValidationError("The 'id' field must be a positive integer")
        
    if not isinstance(data["task"], str) or not data["task"].strip():
        raise ValidationError("The 'task' field must be a non-empty string")

def process_batch(items: list) -> dict:
    """Processes a batch of items, enforcing strict validation on each entry."""
    results = {"processed": [], "rejected": []}
    
    for index, item in enumerate(items):
        try:
            validate_payload(item)
            results["processed"].append({
                "id": item["id"],
                "status": "completed",
                "task_executed": item["task"].strip()
            })
        except ValidationError as error:
            results["rejected"].append({
                "index": index,
                "reason": str(error),
                "data": item
            })
            
    return results