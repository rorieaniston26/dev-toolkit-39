import logging
import sys
from typing import Optional

class DataLogger:
    """Utility class for standardized data logging across dev-toolkit-39."""
    
    def __init__(self, name: str = "dev-toolkit", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Prevent duplicate handlers if re-initialized
        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            stream_handler = logging.StreamHandler(sys.stdout)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

    def info(self, message: str, data: Optional[dict] = None) -> None:
        log_msg = f"{message} | Data: {data}" if data else message
        self.logger.info(log_msg)

    def error(self, message: str, exc: Optional[Exception] = None) -> None:
        self.logger.error(f"{message} | Exception: {str(exc)}" if exc else message)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

# Singleton instance for general usage
logger = DataLogger()