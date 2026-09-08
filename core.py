import logging

# Configure logger for dev-toolkit-39
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

def validate_input(data):
    """Ensures input data conforms to expected structure."""
    if not isinstance(data, dict):
        return False
    if 'id' not in data or not isinstance(data['id'], int):
        return False
    return True

def run_processor(data_stream):
    """Main processing loop with input validation."""
    for entry in data_stream:
        if not validate_input(entry):
            logger.warning(f"Invalid record skipped: {entry}")
            continue
        
        try:
            # Process valid entry
            processed_val = entry['id'] * 2
            logger.info(f"Processing ID {entry['id']} -> {processed_val}")
        except Exception as e:
            logger.error(f"Unexpected error processing record: {e}")

if __name__ == '__main__':
    sample_data = [
        {'id': 1}, 
        {'id': 'invalid'},
        {'id': 42},
        'not-a-dict'
    ]
    run_processor(sample_data)