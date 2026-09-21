import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance with consistent formatting.

    :param name: The name of the logger module
    :param level: Logging severity level (default INFO)
    :return: A configured logging.Logger object
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    formatter: logging.Formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

def log_event(logger: logging.Logger, message: str, level: str = "info") -> None:
    """
    Helper to log messages at specific levels dynamically.

    :param logger: Logger instance to use
    :param message: The text content to log
    :param level: The severity level (info, warning, error)
    """
    levels: dict = {
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error
    }
    
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)

if __name__ == "__main__":
    dev_logger = setup_logger("dev-toolkit")
    log_event(dev_logger, "logger initialized successfully")