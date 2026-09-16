import logging

# Configure standard logger for processor module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

def validate_input(data):
    """Ensures input data conforms to expected schema."""
    if not isinstance(data, dict):
        raise ValueError("input must be a dictionary")
    if 'id' not in data or 'payload' not in data:
        raise KeyError("missing required fields: id, payload")
    if not isinstance(data['id'], int):
        raise TypeError("id must be an integer")
    return True

def run_processing_loop(data_stream):
    """Main loop with integrated input validation logic."""
    for entry in data_stream:
        try:
            if validate_input(entry):
                logger.info(f"Processing entry {entry['id']}")
                # Actual processing logic would follow here
        except (ValueError, KeyError, TypeError) as e:
            logger.error(f"Validation failed for input {entry}: {e}")
            continue

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'payload': 'test_data_a'},
        {'id': 'invalid', 'payload': 'oops'},
        {'id': 2, 'payload': 'test_data_b'}
    ]
    run_processing_loop(sample_data)