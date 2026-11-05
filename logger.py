import logging
import sys
from typing import Optional

class AppLogger:
    """Custom logger implementation for dev-toolkit-39."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log informational messages to standard output."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[bool] = False) -> None:
        """Log error messages with optional traceback details."""
        self.logger.error(message, exc_info=exc_info)

def get_logger(name: str = "dev-toolkit") -> AppLogger:
    """Factory function to retrieve a configured logger instance."""
    return AppLogger(name)