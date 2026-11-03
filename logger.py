import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'app.log', level: int = logging.INFO):
    """
    configures a rotating file logger for dev-toolkit-39
    max size: 5MB, keeps 3 backups
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # prevent adding multiple handlers on re-import
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # rotating handler: 5MB per file, 3 backups
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # stream handler for console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# example usage
if __name__ == '__main__':
    logger = setup_logger('dev-toolkit-39')
    logger.info('logger initialization successful')