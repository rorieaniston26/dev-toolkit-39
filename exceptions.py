class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_payload(data):
    """
    Validates core processing data structure.
    Ensure mandatory fields are present and types match.
    """
    required_fields = {"id": int, "payload": str}
    
    if not isinstance(data, dict):
        raise ValidationError("Data must be a dictionary")
    
    for field, field_type in required_fields.items():
        if field not in data:
            raise ValidationError(f"Missing field: {field}")
        if not isinstance(data[field], field_type):
            raise ValidationError(f"Invalid type for {field}, expected {field_type.__name__}")

def process_main_loop(items):
    """
    Main processing loop with integrated validation logic.
    """
    results = []
    for index, item in enumerate(items):
        try:
            validate_payload(item)
            # Mock processing step
            results.append(f"processed_{item['id']}")
        except ValidationError as e:
            print(f"Skipping item {index}: {e}")
            continue
    return results