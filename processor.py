import logging

# configure basic logging for dev-toolkit-39
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """ensure input is a non-empty dictionary"""
    if not isinstance(data, dict):
        raise ValueError("input must be a dictionary")
    if not data:
        raise ValueError("input dictionary cannot be empty")
    return True

def run_processing_loop(data_stream):
    """main execution loop with integrated validation"""
    for item in data_stream:
        try:
            if validate_input(item):
                # proceed with core logic
                result = item.get("value", 0) * 2
                logger.info(f"processed item: {result}")
        except (ValueError, TypeError) as e:
            logger.error(f"validation failed for item {item}: {e}")
            continue

if __name__ == "__main__":
    # simulation of external data source
    sample_stream = [{"value": 10}, {}, "invalid_format", {"value": 20}]
    run_processing_loop(sample_stream)