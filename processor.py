import logging

# Configure basic logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

def validate_payload(data):
    """Ensures payload is a dict with non-empty keys."""
    if not isinstance(data, dict):
        raise ValueError("Payload must be a dictionary")
    if 'task_id' not in data or not isinstance(data['task_id'], int):
        raise ValueError("Invalid or missing task_id")
    return True

def run_processing_loop(task_queue):
    """Main loop with integrated input validation."""
    logger.info("Starting processor loop")
    
    for item in task_queue:
        try:
            # Validate current item structure
            validate_payload(item)
            
            # Execute core business logic
            result = f"processed-{item['task_id']}"
            logger.info(f"Successfully processed {result}")
            
        except (ValueError, KeyError) as e:
            # Log validation errors and continue
            logger.warning(f"Validation failure: {e}")
            continue
        except Exception as e:
            # Log unexpected runtime errors
            logger.error(f"Unexpected loop error: {e}")
            break

if __name__ == '__main__':
    mock_queue = [{'task_id': 1}, {'bad_data': 'test'}, {'task_id': 2}]
    run_processing_loop(mock_queue)