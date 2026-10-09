import logging

logger = logging.getLogger(__name__)

def validate_input_data(data: dict) -> bool:
    """Validates dictionary input for required keys and types."""
    required_fields = {"id": int, "payload": str}
    
    try:
        for field, expected_type in required_fields.items():
            if field not in data:
                logger.error(f"missing required field: {field}")
                return False
            if not isinstance(data[field], expected_type):
                logger.error(f"invalid type for {field}: expected {expected_type}")
                return False
        return True
    except Exception as e:
        logger.exception(f"unexpected validation error: {e}")
        return False

def process_main_loop(data_list: list):
    """Main processing loop with integrated input validation."""
    for entry in data_list:
        if not isinstance(entry, dict):
            logger.warning("skipping non-dictionary entry")
            continue
            
        if not validate_input_data(entry):
            logger.warning(f"skipping malformed entry: {entry.get('id', 'unknown')}")
            continue
            
        # Process validated data
        payload = entry['payload'].strip()
        logger.info(f"successfully processed id {entry['id']}")
