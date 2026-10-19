import logging

# Configure basic logging for the toolkit
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

def validate_input(data):
    """Ensures input is a non-empty dictionary."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if not data:
        raise ValueError("Input cannot be empty")
    if 'task_id' not in data:
        raise KeyError("Missing required field: task_id")
    return True

def process_tasks(task_queue):
    """Main processing loop with integrated input validation."""
    for entry in task_queue:
        try:
            # Validate entry before processing
            validate_input(entry)
            
            # Execution logic for validated task
            task_id = entry['task_id']
            logger.info(f"Processing task: {task_id}")
            
        except (ValueError, KeyError) as e:
            logger.error(f"Skipping invalid task: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during task execution: {e}")

if __name__ == '__main__':
    sample_queue = [
        {'task_id': 101, 'action': 'sync'},
        {},
        {'task_id': 102}
    ]
    process_tasks(sample_queue)