import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str, log_file: str = 'app.log') -> logging.Logger:
    """
    Initialize a rotating logger with a standard formatter.
    Keeps 3 files of 1MB each.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Rotating file handler configuration
        handler = RotatingFileHandler(
            log_file,
            maxBytes=1_000_000,
            backupCount=3
        )
        
        # Standard formatting with timestamps
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Optional: add console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger