import logging
import os
import sys

class CustomLogger:
    """Thread-safe logger with edge-case handling for file system access."""
    def __init__(self, log_file: str = "app.log"):
        self.log_file = log_file
        self.logger = logging.getLogger("dev-toolkit-39")
        self._setup_logger()

    def _setup_logger(self):
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        try:
            # Handle restricted directory permissions or read-only filesystems
            file_handler = logging.FileHandler(self.log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        except (OSError, IOError) as e:
            # Fallback to stdout if file logging fails due to permissions/disk full
            stream_handler = logging.StreamHandler(sys.stderr)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)
            self.logger.error(f"failed to initialize file logging: {e}. defaulting to stderr.")

    def log_message(self, message: str, level: str = "info"):
        """Logs message with safe string sanitization for binary data."""
        if not isinstance(message, str):
            message = str(message)
            
        try:
            getattr(self.logger, level.lower())(message)
        except AttributeError:
            self.logger.warning(f"invalid log level requested: {level}. using info.")
            self.logger.info(message)
        except Exception as e:
            sys.stderr.write(f"critical error during logging: {str(e)}\n")