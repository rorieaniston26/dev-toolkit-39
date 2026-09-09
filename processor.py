import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary with required keys."""
    if not isinstance(data, dict):
        return False, "Input must be a dictionary"
    if 'id' not in data or 'payload' not in data:
        return False, "Missing required keys: id, payload"
    if not isinstance(data['id'], int):
        return False, "Invalid id type"
    return True, None

def process_items(items):
    """Main processing loop with validation."""
    for index, item in enumerate(items):
        is_valid, error = validate_input(item)
        
        if not is_valid:
            logger.warning(f"Skipping invalid item at index {index}: {error}")
            continue
        
        try:
            # Simulate processing logic
            result = f"Processed {item['id']}: {item['payload']}"
            logger.info(result)
        except Exception as e:
            logger.error(f"Critical error processing item {item['id']}: {e}")

if __name__ == "__main__":
    data_stream = [
        {'id': 1, 'payload': 'task_alpha'},
        {'invalid': 'data'},
        {'id': 2, 'payload': 'task_beta'}
    ]
    process_items(data_stream)