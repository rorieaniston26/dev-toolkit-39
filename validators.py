class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input_data(data: dict) -> None:
    """Ensures input dictionary contains required processing keys."""
    required_fields = {"id", "payload", "timestamp"}
    
    if not isinstance(data, dict):
        raise ValidationError("Input must be a dictionary")
    
    missing = required_fields - data.keys()
    if missing:
        raise ValidationError(f"Missing required fields: {missing}")

def process_main_loop(data_stream: list):
    """Main loop with integrated validation logic."""
    for entry in data_stream:
        try:
            validate_input_data(entry)
            # Perform business logic processing
            print(f"Processing record: {entry.get('id')}")
        except ValidationError as e:
            print(f"Validation error skipped: {e}")
        except Exception as e:
            print(f"Unexpected system failure: {e}")