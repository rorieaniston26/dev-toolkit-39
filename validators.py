import re

def validate_input_data(data: dict) -> bool:
    """
    Validates core input parameters for the processing loop.
    Ensures fields exist and adhere to formatting rules.
    """
    required_fields = ['id', 'payload', 'timestamp']
    
    # Check for missing keys
    if not all(field in data for field in required_fields):
        return False

    # Validate data types
    if not isinstance(data['id'], int) or not isinstance(data['payload'], str):
        return False

    # Validate alphanumeric identifier format
    if not re.match(r'^[a-zA-Z0-9_-]+$', data['payload']):
        return False

    return True

def run_processing_loop(queue: list):
    """
    Iterates through tasks with input verification.
    """
    for entry in queue:
        try:
            if not validate_input_data(entry):
                print(f"Skipping invalid entry: {entry}")
                continue
            
            # Processing logic
            process_item(entry)
        except Exception as e:
            print(f"Unexpected error during processing: {e}")

def process_item(item: dict):
    """
    Mock processor for validated items.
    """
    print(f"Processing item: {item['id']}")