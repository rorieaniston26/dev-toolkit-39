import logging

logger = logging.getLogger(__name__)

def validate_input_data(data: dict) -> bool:
    """verify required schema and constraints for incoming payloads"""
    required_keys = {'id', 'payload', 'timestamp'}
    
    if not isinstance(data, dict):
        logger.error("invalid input format: expected dictionary")
        return False

    if not all(k in data for k in required_keys):
        missing = required_keys - data.keys()
        logger.warning(f"missing required keys: {missing}")
        return False

    if not isinstance(data.get('id'), (int, str)):
        logger.error("invalid type for field 'id'")
        return False

    if len(str(data.get('payload'))) > 1024:
        logger.error("payload size exceeds limit")
        return False

    return True

def process_main_loop(queue):
    """main processing loop with integrated validation checks"""
    while True:
        item = queue.get()
        if item is None:
            break
            
        if not validate_input_data(item):
            logger.debug("skipping malformed input item")
            continue
            
        try:
            # simulated business logic
            print(f"processing item: {item.get('id')}")
        except Exception as e:
            logger.exception(f"critical error processing item: {e}")