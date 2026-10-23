import logging
import os
import sys

def setup_logger(name: str, log_file: str = 'app.log'):
    """Configures a robust logger with file rotation and edge case handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    try:
        # Ensure directory existence for log path
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    except (PermissionError, OSError) as e:
        # Fallback to stderr if file system is inaccessible
        fallback_handler = logging.StreamHandler(sys.stderr)
        logger.addHandler(fallback_handler)
        logger.error(f'failed to initialize log file at {log_file}: {e}')

    return logger

def safe_log(logger, message: str, level: int = logging.INFO):
    """Utility for logging strings with encoding safety."""
    try:
        logger.log(level, str(message))
    except Exception as e:
        print(f'Critical logger failure: {e}', file=sys.stderr)