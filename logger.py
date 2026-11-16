import logging
import sys
from typing import Optional

class DevLogger:
    """Standardized logging utility for dev-toolkit-39."""
    
    def __init__(self, name: str = "dev-toolkit", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[Exception] = None) -> None:
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

def get_logger(name: str = "dev-toolkit") -> DevLogger:
    """Factory function for logger instantiation."""
    return DevLogger(name)