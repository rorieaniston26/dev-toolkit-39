import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

def validate_input(data):
    """Ensures input is a non-empty dictionary with string keys."""
    if not isinstance(data, dict) or not data:
        return False
    return all(isinstance(k, str) for k in data.keys())

def process_payloads(payload_list):
    """Main processing loop with integrated input validation."""
    for index, item in enumerate(payload_list):
        if not validate_input(item):
            logger.error(f"validation failed at index {index}: {item}")
            continue
        
        try:
            # Simulate business logic
            logger.info(f"processing item: {item.get('id', 'unknown')}")
            process_data(item)
        except Exception as e:
            logger.error(f"runtime error at index {index}: {str(e)}")

def process_data(data):
    """Placeholder for actual processing logic."""
    pass

if __name__ == '__main__':
    sample_data = [{'id': 'task-1'}, 'invalid', {'type': 'report'}]
    process_payloads(sample_data)