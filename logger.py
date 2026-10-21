import logging
import os
import sys
from typing import Optional

def setup_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
    """Configures a standardized logger with robust file handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler with error checking for invalid paths
    if log_file:
        try:
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)
            
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (OSError, IOError) as e:
            logger.error(f"failed to initialize log file {log_file}: {e}")
            # Fallback to stderr for critical visibility
            print(f"Critical: Logger fallback due to {e}", file=sys.stderr)

    return logger