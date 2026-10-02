import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = "dev-toolkit.log", level: int = logging.INFO):
    """Configures a rotating file logger for project dev-toolkit-39."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is initialized multiple times
    if not logger.handlers:
        # Rotation: 5MB per file, keep 3 backup files
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
        
        # Optional: Add stream handler for console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

if __name__ == "__main__":
    log = setup_logger("dev-toolkit-39")
    log.info("logger initialized successfully")