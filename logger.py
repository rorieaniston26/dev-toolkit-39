import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str, log_file: str = 'app.log') -> logging.Logger:
    """Configures a rotating file logger for dev-toolkit-39."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if get_logger is called multiple times
    if not logger.handlers:
        # Setup rotating file handler: 5MB max, keep 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        # Optional: Add console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger