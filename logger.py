import logging
from logging.handlers import RotatingFileHandler
import os

# Logging directory setup
LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'app.log')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def setup_logger(name: str = 'dev-toolkit-39', level: int = logging.INFO):
    """Initializes a logger with file rotation."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        # Rotating handler: max 5MB per file, keep 3 backups
        handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Optional console stream
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Global instance for project-wide use
logger = setup_logger()