import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

def validate_input(data):
    """Ensures input is a non-empty dictionary."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    return True

def run_processing_loop(data_stream):
    """Main loop with validation logic."""
    for item in data_stream:
        try:
            if validate_input(item):
                result = item.get('value', 0) * 2
                logger.info(f"Processed value: {result}")
        except ValueError as e:
            logger.error(f"Validation error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    mock_data = [{'value': 10}, {}, 'invalid', {'value': 20}]
    run_processing_loop(mock_data)