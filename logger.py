import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance with a formatted stream handler.

    :param name: The name of the logger instance.
    :param level: The logging threshold level.
    :return: A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_message(logger: logging.Logger, message: str, level: str = "info") -> None:
    """
    Logs a message at the specified level.

    :param logger: The logger instance to use.
    :param message: The string message to record.
    :param level: The log level as a string (debug, info, warning, error).
    """
    levels = {
        "debug": logger.debug,
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
    }
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)