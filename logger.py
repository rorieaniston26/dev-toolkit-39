import logging
from logging.handlers import RotatingFileHandler
import sys

def setup_logger(name: str = 'dev-toolkit', log_file: str = 'app.log'):
    """Initializes a rotating file logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotation setup: 5MB per file, keep 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Stream to console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger