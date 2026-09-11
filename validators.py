import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

def validate_input(data: dict) -> bool:
    """Ensures input data contains mandatory fields and valid types."""
    required_fields = {'id': int, 'payload': str}
    
    for field, expected_type in required_fields.items():
        if field not in data:
            logger.error(f'Missing field: {field}')
            return False
        if not isinstance(data[field], expected_type):
            logger.error(f'Invalid type for {field}: expected {expected_type}')
            return False
    return True

def run_processor(stream):
    """
    Main processing loop with integrated input validation.
    Processes valid data entries from the provided stream.
    """
    for entry in stream:
        try:
            if not validate_input(entry):
                continue
                
            # Simulate business logic processing
            processed_id = entry['id'] * 2
            logger.info(f'Successfully processed ID: {processed_id}')
            
        except Exception as e:
            logger.critical(f'Unexpected error during loop iteration: {e}')

if __name__ == '__main__':
    mock_stream = [{'id': 1, 'payload': 'test'}, {'id': 'bad', 'payload': 'fail'}, {'id': 2, 'payload': 'ok'}]
    run_processor(mock_stream)