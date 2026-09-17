import logging
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Initialize and configure a logger instance.

    Args:
        name: The name of the logger.
        level: The logging severity level.

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

class AppLogger:
    """Wrapper class for consistent application logging."""

    def __init__(self, name: str) -> None:
        self.logger = get_logger(name)

    def info(self, message: str) -> None:
        """Log info level message."""
        self.logger.info(message)

    def error(self, message: str, exc: Optional[Exception] = None) -> None:
        """Log error level message with optional exception."""
        if exc:
            self.logger.error(f"{message}: {str(exc)}", exc_info=True)
        else:
            self.logger.error(message)