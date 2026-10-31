import logging
import sys
from typing import Optional

class AppLogger:
    """Standardized logging utility for dev-toolkit-39."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log informational messages to stdout."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[bool] = False) -> None:
        """Log error messages with optional stack trace."""
        self.logger.error(message, exc_info=exc_info)

def get_logger(name: str) -> AppLogger:
    """Factory function for creating logger instances."""
    return AppLogger(name)
