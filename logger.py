import logging
import os
import sys
from typing import Optional

def get_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
    """Configures a robust logger with file fallback."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Attempt file logging with permission edge case handling
    if log_file:
        try:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (OSError, IOError) as e:
            sys.stderr.write(f"Failed to initialize log file {log_file}: {e}\n")

    # Fallback to console if needed
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

def safe_log_write(logger: logging.Logger, message: str) -> None:
    """Safely logs messages handling potential encoding issues."""
    try:
        logger.info(message)
    except UnicodeEncodeError:
        # Sanitize message if encoding fails
        clean_msg = message.encode('ascii', 'ignore').decode('ascii')
        logger.info(f"[Sanitized] {clean_msg}")
    except Exception as e:
        sys.stderr.write(f"Critical logging failure: {e}\n")