import logging
import sys
from typing import Optional

class AppLogger:
    """Custom logger implementation for dev-toolkit-39."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log informational message."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[Exception] = None) -> None:
        """Log error message with optional traceback."""
        self.logger.error(message, exc_info=exc_info)

    def debug(self, message: str) -> None:
        """Log debug diagnostic message."""
        self.logger.debug(message)

def get_logger(name: str) -> AppLogger:
    """Factory function to instantiate application logger."""
    return AppLogger(name)